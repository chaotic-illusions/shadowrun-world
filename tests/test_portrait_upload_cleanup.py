"""Replacing a portrait deletes the old uploaded file, never anything outside the upload dir."""
import asyncio
import io
from contextlib import asynccontextmanager

from fastapi import UploadFile
from PIL import Image
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from starlette.datastructures import Headers

from app.auth.core import hash_token
from app.db.base import Base
from app.models.character import Character
from app.routers.characters import upload_character_portrait

OWNER = {"is_admin": False, "is_user": True, "user_token": "runner", "view_as_player": False}


@asynccontextmanager
async def _database(path):
    engine = create_async_engine(f"sqlite+aiosqlite:///{path.as_posix()}", connect_args={"timeout": 5})
    sessions = async_sessionmaker(engine, expire_on_commit=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    try:
        yield sessions
    finally:
        await engine.dispose()


def _png() -> UploadFile:
    buf = io.BytesIO()
    Image.new("RGB", (2, 2)).save(buf, format="PNG")
    buf.seek(0)
    return UploadFile(file=buf, filename="p.png", headers=Headers({"content-type": "image/png"}))


def test_second_upload_removes_first_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    portraits = tmp_path / "data" / "uploads" / "portraits"
    portraits.mkdir(parents=True)
    keep = tmp_path / "data" / "keep.txt"
    keep.write_text("not a portrait")

    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            async with sessions() as db:
                db.add(Character(id=1, name="Runner", is_pc=True, owner_token=hash_token("runner"),
                                 portrait_url="/uploads/portraits/../../keep.txt"))
                await db.commit()
            async with sessions() as db:
                first = (await upload_character_portrait(1, file=_png(), db=db, ctx=OWNER))["portrait_url"]
            async with sessions() as db:
                second = (await upload_character_portrait(1, file=_png(), db=db, ctx=OWNER))["portrait_url"]
            return first, second

    first, second = asyncio.run(scenario())
    assert [p.name for p in portraits.iterdir()] == [second.rsplit("/", 1)[1]]
    assert first != second
    assert keep.exists()  # a non-upload portrait_url is never treated as a path to delete
