from sqlalchemy import Boolean, Column, DateTime, Integer, String, func
from sqlalchemy.orm import relationship

from extensions import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    email = Column(String(120), unique=True, nullable=False)
    first_name = Column(String(50))
    is_admin = Column(Boolean, default=False)
    last_name = Column(String(50))
    password = Column(String(255), nullable=False)
    roles = relationship("RoleModel", secondary="user_roles", backref="users")
    username = Column(String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"
