from fastapi import APIRouter, HTTPException, Query
from app.data.consequence_tags import get_tag_info, SINGLE_TAG_RULES
from app.services.consequence_engine import suggest

router = APIRouter()


@router.get("/tags", summary="List all available consequence tags")
def list_tags():
    return {
        "tags": [
            {"tag": tag, "severity": info["severity"]}
            for tag, info in SINGLE_TAG_RULES.items()
        ]
    }


@router.get("/suggest", summary="Get consequence suggestions for a set of tags")
def get_suggestions(
    tags: list[str] = Query(..., description="One or more outcome tags"),
):
    suggestions = suggest(tags)
    return {
        "tags": tags,
        "suggestion_count": len(suggestions),
        "suggestions": suggestions,
    }


@router.get("/tags/{tag}", summary="Get details for a specific tag")
def get_tag(tag: str):
    info = get_tag_info(tag)
    if not info:
        raise HTTPException(status_code=404, detail=f"Unknown tag: {tag}")
    return {"tag": tag, **info}
