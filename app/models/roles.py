import enum
from datetime import datetime

from sqlalchemy import (Column, DateTime, Enum, ForeignKey, Integer, String,
                        Table)

from extensions import Base


class RoleType(enum.Enum):
    COMMUNITY_ADVOCATE = "COMMUNITY_ADVOCATE"
    CASE_MANAGER = "CASE_MANAGER"
    SEXUAL_ASSAULT_ADVOCATE = "SEXUAL_ASSAULT_ADVOCATE"


class RoleModel(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(Enum(RoleType), unique=True, nullable=False)
