from datetime import datetime
from pydantic import BaseModel, validator
from typing import Optional

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class Workout(BaseModel):

    id:  Optional[str]
    athlete_id: int
    coach_id: int
    name: str
    start_date_time: str
    end_date_time: str

    @validator('start_date_time')
    def start_date_time_format(cls, v):
        try:
            datetime.strptime(v, DATE_FORMAT)
        except ValueError:
            raise ValueError("Incorrect data format, must be YYYY-MM-DD H:M:S")
        return v

    @validator('end_date_time')
    def end_date_time_format(cls, v):
        try:
            datetime.strptime(v, DATE_FORMAT)
        except ValueError:
            raise ValueError("Incorrect data format, must be YYYY-MM-DD H:M:S")
        return v

    @validator('end_date_time')
    def start_and_end_valid(cls, v, values, **kwargs):
        if 'start_date_time' in values:
            start = datetime.strptime(values['start_date_time'], DATE_FORMAT)
            end = datetime.strptime(v, DATE_FORMAT)
            if start >= end:
                raise ValueError('start_date_time must be before end_date_time')
        return v
