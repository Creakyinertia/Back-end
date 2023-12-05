from pydantic import BaseModel,constr

class student(BaseModel):
    name: str
    dob: str
    age:int
    phone: int
    address:str
    classname:int
    email:str
    course_name:str
    class Config:
        orm_mode = True


class course(BaseModel):
    id:int
    course_name:str
    description:str  
    class Config:
        orm_mode = True

class mobmail(BaseModel):
    phone:int
    email:str