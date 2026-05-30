from pydantic import BaseModel, ConfigDict, Field


class DeckBuilderStateUpdate(BaseModel):
    model_config = ConfigDict(extra='forbid')
    state: dict = Field(default_factory=dict)


class DeckBuilderStateRead(BaseModel):
    state: dict = Field(default_factory=dict)
