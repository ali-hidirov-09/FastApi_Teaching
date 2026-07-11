from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.sql.functions import session_user

from models import User
from sqlalchemy.orm import selectinload, joinedload

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, user_obj):
        user_data = user_obj.model_dump()
        user_info = User(**user_data)

        self.session.add(user_info)
        await self.session.commit()
        await self.session.refresh(user_info)
        return user_info


    async def get_users_with_jobs(self):
    # N+1 muammosini oldini olish uchun selectinload ishlatildi
        query = select(User).options(selectinload(User.jobs))
        result = await self.session.execute(query)
        return result.scalars().all()


# lazy loading - n+1
# eager loading 1+1

