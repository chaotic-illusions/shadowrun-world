from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.models.matrix_host import MatrixHost
from app.schemas.matrix_host import (
    MatrixHostCreate, MatrixHostUpdate, MatrixHostRead, MatrixHostSummary,
    MatrixHostConfig,
)
from app.auth.dependencies import get_admin_token
from app.services.matrix_generator import generate, IC_INFO, VALID_CONNECTIONS

router = APIRouter()


async def _get_or_404(db: AsyncSession, host_id: int) -> MatrixHost:
    result = await db.execute(select(MatrixHost).where(MatrixHost.id == host_id))
    host = result.scalars().first()
    if not host:
        raise HTTPException(status_code=404, detail="Matrix host not found")
    return host


@router.get("/", response_model=list[MatrixHostSummary])
async def list_hosts(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(MatrixHost).order_by(MatrixHost.name))
    return result.scalars().all()


@router.post("/", response_model=MatrixHostRead, status_code=201,
             dependencies=[Depends(get_admin_token)])
async def create_host(body: MatrixHostCreate, db: AsyncSession = Depends(get_db)):
    host = MatrixHost(**body.model_dump())
    db.add(host)
    await db.commit()
    await db.refresh(host)
    return host


@router.post("/generate", response_model=MatrixHostRead, status_code=201,
             dependencies=[Depends(get_admin_token)])
async def generate_host(body: MatrixHostConfig, db: AsyncSession = Depends(get_db)):
    """Generate a topology from parameters, save, and return the full host record."""
    config = body.model_dump()
    topology = generate(config)
    host = MatrixHost(
        name=body.name,
        owner_org_id=body.owner_org_id,
        location_id=body.location_id,
        notes=body.notes,
        config_json=config,
        topology_json=topology,
    )
    db.add(host)
    await db.commit()
    await db.refresh(host)
    return host


@router.get("/ic-info")
async def ic_info():
    """Return IC type metadata (mechanics, flavor) for the frontend tooltip system."""
    return IC_INFO


@router.get("/connection-matrix")
async def connection_matrix():
    """Return the valid connection rules as a serializable dict."""
    return {k: sorted(v) for k, v in VALID_CONNECTIONS.items()}


@router.get("/{host_id}", response_model=MatrixHostRead)
async def get_host(host_id: int, db: AsyncSession = Depends(get_db)):
    return await _get_or_404(db, host_id)


@router.patch("/{host_id}", response_model=MatrixHostRead,
              dependencies=[Depends(get_admin_token)])
async def update_host(
    host_id: int, body: MatrixHostUpdate, db: AsyncSession = Depends(get_db)
):
    host = await _get_or_404(db, host_id)
    updates = body.model_dump(exclude_unset=True)
    for field, value in updates.items():
        setattr(host, field, value)
    await db.commit()
    await db.refresh(host)
    return host


@router.delete("/{host_id}", status_code=204,
               dependencies=[Depends(get_admin_token)])
async def delete_host(host_id: int, db: AsyncSession = Depends(get_db)):
    host = await _get_or_404(db, host_id)
    await db.delete(host)
    await db.commit()
