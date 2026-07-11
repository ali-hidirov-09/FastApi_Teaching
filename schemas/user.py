from pydantic import BaseModel, SecretStr, ConfigDict, Field, EmailStr, model_validator, field_validator
from typing import Annotated
from pydantic.alias_generators import to_camel


class BaseSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        extra='forbid'
    )

MinStr = Annotated[str, Field(min_length=3)]
MinPass = Annotated[str, Field(min_length=8)]


class CreateUser(BaseSchema):
    name: str
    age: int
    email: EmailStr
    password: str