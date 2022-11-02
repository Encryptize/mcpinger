from typing import Union

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
    players: Union[Players, None] = None
    protocol: Union[int, None] = None
    version: Union[str, None] = None
    favicon: Union[str, None] = None
    description: Union[Description, None] = None
