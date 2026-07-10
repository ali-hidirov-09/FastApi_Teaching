from core.database import Base
from sqlalchemy import String,text
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime



class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(server_default=text("CURRENT_TIMESTAMP"))


