class FreelanceHubError(Exception):
    pass

class ObjectNotFound(FreelanceHubError):
    def __init__(self, model_name: str, obj_id: int, status_code: int):
        self.model_name = model_name
        self.obj_id = obj_id
        self.status_code = status_code


class ServerError(FreelanceHubError):
    def __init__(self, status_code: int, message: str):
        self.message = message
        self.status_code = status_code


class NotRegistered(FreelanceHubError):
    def __init__(self, user_id: int, status_code: int):
        self.user_id = user_id
        self.status_code = status_code