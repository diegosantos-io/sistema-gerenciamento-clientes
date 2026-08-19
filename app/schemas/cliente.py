from pydantic import BaseModel,EmailStr, Field

class Cliente(BaseModel):
    nome:str = Field(min_length=3)
    email:EmailStr
    telefone:str = Field(
        min_length= 10, 
        max_length=11,
        pattern=r"^[0-9]+$"
        )
