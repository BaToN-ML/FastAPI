from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from app.database.db import Base


class House(Base):
    """Модель дома."""

    __tablename__ = "houses"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    area: Mapped[int]
    price: Mapped[int]
    location: Mapped[Optional[str]]
    metro: Mapped[Optional[str]]
