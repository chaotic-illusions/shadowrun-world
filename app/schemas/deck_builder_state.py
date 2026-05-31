import json

from pydantic import BaseModel, ConfigDict, Field, field_validator

# Upper bound on a persisted deck-builder blob. Players can write this column
# freely (PUT /characters/{id}/deck-builder-state), so cap it to keep a single
# row from being abused as unbounded storage.
MAX_STATE_BYTES = 256 * 1024  # 256 KB


class DeckBuilderStateUpdate(BaseModel):
    model_config = ConfigDict(extra='forbid')
    state: dict = Field(default_factory=dict)

    @field_validator("state")
    @classmethod
    def _limit_size(cls, v: dict) -> dict:
        size = len(json.dumps(v, separators=(",", ":")).encode("utf-8"))
        if size > MAX_STATE_BYTES:
            raise ValueError(
                f"deck_builder_state is too large ({size} bytes; "
                f"limit {MAX_STATE_BYTES} bytes)"
            )
        return v


class DeckBuilderStateRead(BaseModel):
    state: dict = Field(default_factory=dict)
