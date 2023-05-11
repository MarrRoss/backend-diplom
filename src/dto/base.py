from pydantic import BaseModel


class BaseSchema(BaseModel):
    def exclude_optional_dict(self):
        return {**self.dict(exclude_unset=True), **self.dict(exclude_none=True)}

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
