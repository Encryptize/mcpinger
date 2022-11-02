from pydantic import BaseModel


class Players(BaseModel):
    online: int
    max: int

class Description(BaseModel):
    raw: str
    text: str
    normalized: str


class Status(BaseModel):
    online: bool
    ip: str
    players: Players | None = None
    protocol: int | None = None
    version: str | None = None
    favicon: str | None = None
    description: Description | None = None
