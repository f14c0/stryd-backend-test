from pydantic import BaseModel


class Workout(BaseModel):
    athlete_id: int
    coach_id: int
    name: str
    start_date_time: str
    end_date_time: str
