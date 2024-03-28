from pydantic import BaseModel


class ClashUser(BaseModel):
    id: str
    username: str
    townhall_level: int
    player_tag: str
