from typing import Optional
from pydantic import BaseModel

class Digital_solutions_11(BaseModel):
    id: Optional[int] = None
    name: str
    birthdate: str
    area: str
    edv: int
    fav_ice_cream: str
    