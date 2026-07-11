from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import Job
from sqlalchemy.orm import joinedload


class JobRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_jobs(self) -> list[Job]:
        query = select(Job)
        results = await self.session.execute(query)
        return list(results.scalars().all())


    async def get_job_by_id(self, job_id: int):
        query = select(Job).where(Job.id == job_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def create_job(self, job_obj):
        job_data = job_obj.model_dump()
        job_data['owner_id'] = 1
        info_job = Job(**job_data)

        self.session.add(info_job)
        await self.session.commit()
        await self.session.refresh(info_job)
        return info_job


    async def update(self, job_id: int, update_data: dict):
        db_obj = await self.get_job_by_id(job_id)

        if db_obj:
            for key, value in update_data.items():
                if hasattr(db_obj, key):
                    setattr(db_obj, key, value)
            await self.session.commit()
            await self.session.refresh(db_obj)
        return db_obj


    async def delete(self, job_id: int):
        db_obj = await self.get_job_by_id(job_id)

        if db_obj:
            await self.session.delete(db_obj)
            await self.session.commit()
            return True
        return False

    async def get_jobs_with_user(self):
    # N+1 muammosini oldini olish uchun selectinload ishlatildi
        query = select(Job).options(joinedload(Job.user))
        result = await self.session.execute(query)
        return result.scalars().all()



