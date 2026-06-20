#
#
#
#
#
#
#
#
#
# async def test_get_all():
#     async with async_session_maker() as session:
#         repo = JobRepository(session)
#         jobs = await repo.get_all()
#         print(jobs)
#
#
# async def test_get_by_id(id):
#     async with async_session_maker() as session:
#         repo = JobRepository(session)
#         jobs = await repo.get_by_id(id)
#         print(jobs)
#
#
# async def test_create(data):
#     async with async_session_maker() as session:
#         repo = JobRepository(session)
#         jobs = await repo.create(data)
#         print(jobs)
#
#
# async def test_update(id, data):
#     async with async_session_maker() as session:
#         repo = JobRepository(session)
#         jobs = await repo.update(id, data)
#         print(jobs)
#
#
# async def test_delete(id):
#     async with async_session_maker() as session:
#         repo = JobRepository(session)
#         jobs = await repo.delete(id)
#         print(jobs)
#
#
#
# data_job = Job(
#     title="Python Developer",
#     description="Junior backend",
#     salary=1200
# )
# data_job2 = {
#     "description": "Bizga Pythonda fast api da mustaqil kod yoza oladigan  senior developer kerak",
#     "title": "Backend developer",
#     "salary": 5000
# }
#
#
#
#
# async def main():
#     await test_get_all()
#     await  test_create(data_job)
#     await  test_get_by_id(2)
#     await  test_update(2, data_job2)
#     await  test_get_by_id(2)
#     await  test_delete(2)
#     await  test_get_by_id(2)
#
# asyncio.run(main())