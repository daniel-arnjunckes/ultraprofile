from pydantic import BaseModel

class Profile(BaseModel):
    
    name:           str
    age:            int
    description:    str
        
class ProfileRequest(Profile):
    ...

class ProfileResponse(Profile):
    id:             int
    class Config:
        orm_mode = True
