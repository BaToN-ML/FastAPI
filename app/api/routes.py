from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.db import get_session
from app.repositories import HouseRepository
from app.schemas import HouseCreate, HouseID, HouseRead

router = APIRouter(prefix="/houses", tags=["houses"])

SessionDep = Annotated[AsyncSession, Depends(get_session)]


@router.post("", response_model=HouseID, status_code=201)
async def add_house(data: HouseCreate, session: SessionDep) -> HouseID:
    """Создать новый дом."""
    house_id = await HouseRepository.add_house(session, data)
    return HouseID(house_id=house_id)


@router.get("", response_model=list[HouseRead])
async def get_houses(session: SessionDep) -> list[HouseRead]:
    """Получить список всех домов."""
    return await HouseRepository.get_all(session)