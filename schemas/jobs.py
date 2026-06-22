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





class Account(BaseSchema):
    username: MinStr
    password: MinStr
    confirm_password:MinPass
    salary_min: float = Field(ge=500)
    salary_max: float = Field(ge=500.0)


    @model_validator(mode='after')
    def check_passwords(self):
        if self.password != self.confirm_password:
            raise ValueError("Parollar bir biriga mos kelamydi")
        return self

    @field_validator("username")
    @classmethod
    def check_username(cls, v: str):
        if not v.isalpha():
            raise ValueError("Ism ichida son kelishi mumkin emas")
        return v.title()


    @model_validator(mode='after')
    def check_salaries(self):
        if self.salary_min > self.salary_max:
            raise ValueError("salary_min salary_max dan katta bo'lishi mumkin emas")
        return self


    @model_validator(mode="after")
    def check_password(self):
        if self.username.lower() in self.password.lower():
            raise ValueError("Password ichida username bo'lmasligi kk, bizda xavfsizlik 1-o'rinda")
        return self



