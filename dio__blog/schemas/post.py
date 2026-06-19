from pydantic import BaseModel
from datetime import UTC, datetime

class PostIn(BaseModel):
    title: str
    content: str
    date: datetime = datetime.now(UTC)
    published: bool = False


class PostUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    published: bool | None = None
