from fastapi import FastAPI
from .exception import ObjectNotFound, ServerError, NotRegistered
from .exception_handlers import object_not_found_handler, server_error, not_registered

def setup_exception_handlers(app:FastAPI):
    app.add_exception_handler(ObjectNotFound, object_not_found_handler)
    app.add_exception_handler(ServerError, server_error)
    app.add_exception_handler(NotRegistered, not_registered)
