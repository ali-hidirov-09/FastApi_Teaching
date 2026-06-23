from fastapi import Request
from fastapi.responses import JSONResponse
from .exception import ObjectNotFound, ServerError, NotRegistered

async def object_not_found_handler(request: Request, exc: ObjectNotFound):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": f"{exc.model_name}(id={exc.obj_id}) toplimadi."}
    )

async def server_error(request: Request, exc: ServerError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message}
    )


async def not_registered(request: Request, exc: NotRegistered):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": f"{exc.user_id} id dagi user registratsiya qilinmagan"}
    )