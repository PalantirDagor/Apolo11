from pydantic import BaseModel, Field, validator

class Misiones(BaseModel):
    device_status: str
    device_type: str


