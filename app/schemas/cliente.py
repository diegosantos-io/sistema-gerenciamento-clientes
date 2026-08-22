from pydantic import BaseModel,ConfigDict,EmailStr, Field

class ClienteBase(BaseModel):
    nome:str = Field(min_length=3)

    email:EmailStr

    telefone:str = Field(
        min_length= 10, 
        max_length=11,
        pattern=r"^[0-9]+$"
        )


class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    id:int

    model_config = ConfigDict(from_attributes= True)

