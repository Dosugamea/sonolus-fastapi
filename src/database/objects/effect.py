from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.database.db import Base
from src.database.mixins import SonolusDataMixin, TimeMixin


class Effect(SonolusDataMixin, TimeMixin, Base):  # type: ignore
    __tablename__ = "effects"
    __table_args__ = {"extend_existing": True}

    thumbnail_hash = Column(String(128))
    data_hash = Column(String(128))
    engines = relationship("Engine", back_populates="effect")
    levels = relationship("Level", back_populates="effect")
    user = relationship("User", back_populates="effects", uselist=False)
