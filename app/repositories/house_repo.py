from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import House
from app.schemas import HouseCreate, HouseRead


class HouseRepository:
    """Репозиторий для работы с объектами."""

    @staticmethod
    async def add_house(session: AsyncSession, data: HouseCreate) -> int:
        """Добавить новый дом и вернуть его ID."""
        house = House(**data.model_dump())
        session.add(house)
        await session.commit()
        await session.refresh(house)
        return house.id

    @staticmethod
    async def get_all(session: AsyncSession) -> list[HouseRead]:
        """Получить все дома."""
        result = await session.execute(select(House))
        houses = result.scalars().all()
        return [HouseRead.model_validate(house) for house in houses]
