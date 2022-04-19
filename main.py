from fastapi import FastAPI, status, HTTPException
from database import Database
from workout_scheduler import WorkoutScheduler
from models import Workout

app = FastAPI()
db = Database()
scheduler = WorkoutScheduler()


@app.post("/workouts/", status_code=status.HTTP_201_CREATED)
async def plan_workout(workout: Workout):

    if not db.get_coach_by_id(coach_id=workout.coach_id):
        raise HTTPException(status_code=404, detail="Coach not found")

    if not db.get_athlete_by_id(athlete_id=workout.athlete_id):  # Athlete id should be taken from Auth mechanism..
        raise HTTPException(status_code=404, detail="Athlete not found")

    wo_planned, message = scheduler.plan_workout(workout=workout)
    if not wo_planned:
        raise HTTPException(status_code=400, detail=message)
    return message


@app.post("/coaches/{coach_id}/workouts/", status_code=status.HTTP_201_CREATED)
async def plan_workout(workout: Workout, coach_id: int):

    if not db.get_coach_by_id(coach_id=coach_id):
        raise HTTPException(status_code=404, detail="Coach not found")

    if not db.get_athlete_by_id(athlete_id=workout.athlete_id):  # Athlete id should be taken from Auth mechanism..
        raise HTTPException(status_code=404, detail="Athlete not found")

    wo_planned, message = scheduler.plan_workout(workout=workout)
    if not wo_planned:
        raise HTTPException(status_code=400, detail=message)

    return message


@app.get("/coaches/{coach_id}/workouts")
async def coach_workouts(coach_id: int):
    if not db.get_coach_by_id(coach_id=coach_id):
        raise HTTPException(status_code=404, detail="Coach not found")
    return db.get_coach_workouts(coach_id=coach_id)


@app.get("/athletes/{athlete_id}/workouts")
async def athlete_workouts(athlete_id: int):
    if not db.get_athlete_by_id(athlete_id=athlete_id):
        raise HTTPException(status_code=404, detail="Athlete not found")
    return db.get_athlete_workouts(athlete_id=athlete_id)
