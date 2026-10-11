from typing import Optional

from pydantic import BaseModel, ConfigDict


class HouseCreate(BaseModel):
    """Схема для создания объекта"""

    name: str
    area: int
    price: int
    location: Optional[str] = None
    metro: Optional[str] = None


class HouseRead(HouseCreate):
    """Схема для чтения объекта"""

    id: int
    model_config = ConfigDict(from_attributes=True)


class HouseID(BaseModel):
    """Схема ответа с ID созданного объекта"""

    ok: bool = True
    house_id: int