from typing import Optional

from pydantic import BaseModel

class AppointmentCreate(BaseModel):
    d_id: int
