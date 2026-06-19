from typing import Optional

from fastapi import APIRouter, Path, Query

router = APIRouter()


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