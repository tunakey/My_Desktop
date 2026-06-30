from sqlalchemy import (Boolean, Column, DateTime, Enum, ForeignKey, Integer,
                        String)

from extensions import Base


class UserRoleModel(Base):
    __tablename__ = "user_roles"

    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True
    )
    role_id = Column(
        Integer, ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True
    )
