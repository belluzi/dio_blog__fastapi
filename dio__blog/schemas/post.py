from pydantic import AwareDatetime, BaseModel

class PostIn(BaseModel):
    title: str
    content: str
    date: AwareDatetime | None = None
    published: bool = False


class PostUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    date: AwareDatetime | None = None
    published: bool | None = None
