from typing import Optional
from pydantic import BaseModel

class Whales(BaseModel):
    id: Optional[int] = None
    scientific_name: str
    name: str
    max_weight: str
    max_lenght: str
    name_pt_br: str