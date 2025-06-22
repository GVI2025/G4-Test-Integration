from pydantic import BaseModel

class SalleBase(BaseModel):
    nom: str
    capacité: int
    localisation: str
    disponible: bool

class SalleCreate(SalleBase):
    pass

class SalleUpdate(SalleBase):
    pass

class SalleRead(SalleBase):
    id: str

    class Config:
        orm_mode = True

class SalleDelete(BaseModel):
    pass