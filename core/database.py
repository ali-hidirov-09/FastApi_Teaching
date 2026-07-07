from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

sqlite_url = "sqlite:///./fast_api_teaching.db"

engine = create_engine(sqlite_url, echo=True)

class Base(DeclarativeBase):
    pass