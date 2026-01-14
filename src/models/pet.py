from pydantic import BaseModel, Field
from typing import List

from src.models.tag import Tag
from src.models.category import Category


class Pet(BaseModel):
    name: str
    photo_urls: List[str] = Field(alias="photoUrls")
    id: int | None = None
    category: Category | None = None
    tags: List[Tag] | None = None
    status: str | None = None

    model_config = {
        "populate_by_name": True
    }
