from pydantic import BaseModel
from datetime import datetime


class ModelDetails(BaseModel):

    customer_name: str
    detail_number: str
    detail_name: str
    detail_price: str
    expected_time: datetime

    class Config:
        orm_mode = True
