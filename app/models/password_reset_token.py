from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from extensions import Base


class PasswordResetTokenModel(Base):
    __tablename__ = "password_reset_tokens"

    id = Column(Integer, primary_key=True)
    token = Column(String(100), unique=True, nullable=False, index=True)
    expires_at = Column(DateTime, nullable=False)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    def is_expired(self):
        """Helper method to check if the token is no longer valid."""
        return datetime.utcnow() > self.expires_at

    def __repr__(self):
        return f"<PasswordResetToken {self.token[:8]}... (User: {self.user_id})>"
