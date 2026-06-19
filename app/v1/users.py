from typing import Optional
from pydantic import BaseModel, SecretStr, ConfigDict, Field, EmailStr
from typing import Annotated
from fastapi import APIRouter, Path, Query
from pydantic.alias_generators import to_camel

router = APIRouter()


class BaseSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        extra='forbid'
    )

MinStr = Annotated[str, Field(min_length=3)]
MinInt = Annotated[int, Field(gt=0)]
#------------------------------------------Dars_5------------------------------------------------------------


class UserSchema(BaseSchema):
    username: str = Field(min_length=3)
    is_active: bool = True
    email: EmailStr
    password: SecretStr


user = UserSchema(username="Ali", email="Ali@gmail.com", password="448484646887")
user_data = user.model_dump()
user_data1 = user.model_dump_json(exclude={"password"})
print(user.password.get_secret_value())
print(user_data1)



class JobSchema(BaseSchema):
    id: MinInt
    title: str
    salary_min: float = Field(gt=0)
    salary_max: float = Field(lt=5000)



@router.post('/job')
async def job_create_1(job:JobSchema):
    jod_data = job.model_dump()
    return {
        "message": "Muvaffaqiyatli yaratildi",
        "data": jod_data
    }


@router.post('/user')
async def user_create_1(user:UserSchema):
    user_data = user.model_dump()
    return {
        "message": "Muvaffaqiyatli yaratildi",
        "data": user_data
    }



devs = [
    {
        "id": 1,
        "category":"IT",
        "title": "Python",
        "full_name":"Ali Khidirov",
        "experience": 1,
        "salary": 600.0,
        "description": "Men junior python developerman va kompaniya rivoji uchun hamma narsa qilishga tayyorman."
    }
]

class Job(BaseSchema):
    category: MinStr
    title: MinStr
    is_active: bool = True
    full_name: MinStr
    experience: int | None = None
    salary: float = Field(..., ge=0.0)
    description: MinStr
    created_at: MinStr
    updated_at: MinStr



@router.post('/dev_create')
async def dev_create(job: Job):
    job_data = job.model_dump()
    job_data['id'] = len(devs)+1
    devs.append(job_data)
    print(devs)
    return {"message": "Muvaffaqiyatli yaratildi",
            "data": job_data}




#------------------------------------------Dars_2,3------------------------------------------------------------
@router.get("/get_name")
def get_name():
    return {
        "Ism": "Ali"
    }

users = [
    {"id": 1, "first_name": "Ali", "job": "Programmer"},
    {"id": 2, "first_name": "Muxammad", "job": "Developer"},
    {"id": 3, "first_name": "Miraziz", "job": "Engineer"},
]



@router.post("/get_by/{user_id}")
def get_user(user_id:int):
    for user in users:
        if user['id'] == user_id:
            return user
    else:
        return {
            "message": "Bizda bunday user topilmadi"
        }


jobs = [
    {
        "id": 1,
        "category": "IT",
        "title": "Python Backend Developer",
        "experience": 2,
        "salary": 1000,
        "description":"Bizga 2 yillik tajribaga ega strong junior python backend developer kerak,",
        "texnologiyalar":"Fastapi, Django, SQL, Postgresql, ptb"
    },

     {
        "id": 2,
        "category": "IT",
        "title": "Java Backend Developer",
        "experience": 4,
        "salary": 2000,
        "description":"Bizga 4 yillik tajribaga ega strong middle python backend developer kerak,",
        "texnologiyalar":" SQL, Postgresql, ptb, Java"
    },
]



@router.get("/jobs/{job_id}")
async def get_job_details(
    job_id: int = Path(..., gt=0, title="Ish identifikatori"),
    keyword: str = Query(..., min_length=3, max_length=50),
    experience: Optional[int] = Query(None, ge=0, le=50),
    category: str = Query("all", alias="job-category") ):
    list = []
    for i in jobs:
        if i["id"] == job_id and i["texnologiyalar"].find(keyword) and i["experience"] == experience and category.upper() == i["category"]:
            list.append(i)

    return list


@router.post("/jobs/{job_id}")
async def get_job_details(
    title: str = Query(..., min_length=3,max_length=50),
    experience: int = Query(default=0, ge=0, le=30),
    description: str | None = Query(min_length=10, max_length=500),
    texnologiya: str = Query(min_length=10, max_length=100),
    ):

    job_id = len(jobs)+1

    new_job = {
        "id": job_id,
        "title": title,
        "experience": experience,
        "description":description,
        "texnologiyalar":texnologiya
                  }

    jobs.append(new_job)
    return jobs