from datetime import datetime
from database import Database
from models import Workout

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

day_names = {
    0: "monday",
    1: "tuesday",
    2: "wednesday",
    3: "thursday",
    4: "friday",
    5: "saturday",
    6: "sunday"
}


def _str_to_date(date_str: str):
    return datetime.strptime(date_str, DATE_FORMAT)


class WorkoutScheduler:
    db = Database()

    def plan_workout(self, workout: Workout):
        schedule_validation, errors = self.validate_workout(workout)
        if schedule_validation is True:
            new_wo = self.db.insert_workout(workout.dict())
            return True, {"message": f"Workout created successfully ", "errors": errors, "workout": new_wo}
        return False, {"message": f"could not create workout ", "errors": errors}

    def validate_workout(self, workout: Workout):
        coach_available, c_message = self.validate_coach_availability(new_workout=workout)
        athlete_available, a_message = self.validate_athlete_availability(new_workout=workout)
        return coach_available and athlete_available, c_message + a_message

    def validate_coach_availability(self, new_workout: Workout):
        coach_workouts = self.db.get_coach_workouts(coach_id=new_workout.coach_id)
        new_wo_start = _str_to_date(new_workout.start_date_time)
        new_wo_end = _str_to_date(new_workout.end_date_time)

        # check workout does not collide with coach scheduled workouts
        for existing_wo in coach_workouts:
            existing_wo = Workout(**existing_wo)
            existing_wo_start = _str_to_date(existing_wo.start_date_time)
            existing_wo_end = _str_to_date(existing_wo.end_date_time)

            if self.periods_collide(p1_start=existing_wo_start, p1_end=existing_wo_end,
                                    p2_start=new_wo_start, p2_end=new_wo_end):
                return False, ["workout collides with coach schedule"]

        # check workout does not collide with coach custom unavailable time
        unavailable_times = self.db.get_coach_unavailable_periods(coach_id=new_workout.coach_id,
                                                                  day_mame=day_names.get(new_wo_start.weekday()))
        for u_time in unavailable_times:
            u_time_start = datetime.strptime(f"{new_wo_start.date()} {u_time['start_time']}", DATE_FORMAT)
            u_time_end = datetime.strptime(f"{new_wo_start.date()} {u_time['end_time']}", DATE_FORMAT)

            if self.periods_collide(p1_start=u_time_start, p1_end=u_time_end,
                                    p2_start=new_wo_start, p2_end=new_wo_end):
                return False, ["Coach not available at the time of workout"]

        return True,[]

    def validate_athlete_availability(self, new_workout: Workout):
        athlete_workouts = self.db.get_athlete_workouts(athlete_id=new_workout.athlete_id)
        new_wo_start = _str_to_date(new_workout.start_date_time)
        new_wo_end = _str_to_date(new_workout.end_date_time)

        # check workout does not collide with athlete scheduled workouts
        for existing_wo in athlete_workouts:
            existing_wo = Workout(**existing_wo)
            existing_wo_start = _str_to_date(existing_wo.start_date_time)
            existing_wo_end = _str_to_date(existing_wo.end_date_time)

            if self.periods_collide(p1_start=existing_wo_start, p1_end=existing_wo_end,
                                    p2_start=new_wo_start, p2_end=new_wo_end):
                return False, ["workout collides with athlete schedule"]

        # check workout does not collide with athlete custom unavailable time

        unavailable_times = self.db.get_athlete_unavailable_periods(athlete_id=new_workout.athlete_id,
                                                                    day_mame=day_names.get(new_wo_start.weekday()))

        for u_time in unavailable_times:
            u_time_start = datetime.strptime(f"{new_wo_start.date()} {u_time['start_time']}", DATE_FORMAT)
            u_time_end = datetime.strptime(f"{new_wo_start.date()} {u_time['end_time']}", DATE_FORMAT)

            if self.periods_collide(p1_start=u_time_start, p1_end=u_time_end,
                                    p2_start=new_wo_start, p2_end=new_wo_end):
                return False, ["Athlete not available at the time of workout"]

        return True,[]

    @classmethod
    def periods_collide(cls, p1_start, p1_end, p2_start, p2_end):
        if (p1_start < p2_start) and (p1_end > p2_start):
            return True
        elif p2_start <= p1_start < p2_end:
            return True
        return False
