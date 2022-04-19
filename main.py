from fastapi import FastAPI
from database import Database
from workout_scheduler import WorkoutScheduler
from models import Workout

app = FastAPI()
db = Database()
scheduler = WorkoutScheduler()


@app.post("/workouts/")
async def plan_workout(workout: Workout):
    return scheduler.plan_workout(workout=workout)


@app.get("/coaches/{coach_id}/workouts")
async def coach_workouts(coach_id: int):
    return db.get_coach_workouts(coach_id=coach_id)


@app.get("/athletes/{athlete_id}/workouts")
async def athlete_workouts(athlete_id: int):
    return db.get_athlete_workouts(athlete_id=athlete_id)