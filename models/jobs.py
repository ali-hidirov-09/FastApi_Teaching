from core.database import Base
from sqlalchemy import String, text, NUMERIC, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from decimal import Decimal

class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category: Mapped[str] = mapped_column(String(50))
    title: Mapped[str] = mapped_column(String(50))
    salary: Mapped[Decimal] = mapped_column(NUMERIC(10,2))
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="SET NULL")) # OneToMany
    created_at: Mapped[datetime] = mapped_column(server_default=text("CURRENT_TIMESTAMP"))

    user: Mapped["User"] = relationship(back_populates="jobs")
