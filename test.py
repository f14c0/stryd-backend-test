import pytest
from workout_scheduler import WorkoutScheduler
from models import Workout

cases = [
        ("W1", "2022-04-18 05:00:00", "2022-04-18 06:00:00", True),
        ("W2", "2022-04-18 06:00:00", "2022-04-18 08:00:00", True),
        ("W3", "2022-04-18 14:00:00", "2022-04-18 15:00:00", True),
        ("W4", "2022-04-18 21:00:00", "2022-04-18 22:00:00", True),
        ("W5", "2022-04-19 06:00:00", "2022-04-19 07:00:00", True),
        ("W6", "2022-04-19 13:00:00", "2022-04-19 15:00:00", True),
        ("W7", "2022-04-19 18:00:00", "2022-04-19 19:00:00", True),
        ("W8", "2022-04-19 19:00:00", "2022-04-19 22:00:00", True),
        ("W9", "2022-04-23 05:00:00", "2022-04-23 09:00:00", True),
        ("W10", "2022-04-18 04:00:00", "2022-04-18 05:00:00", False),
        ("W11", "2022-04-19 09:00:00", "2022-04-19 10:00:00", False),
        ("W12", "2022-04-20 14:00:00", "2022-04-20 19:00:00", False),
        ("W13", "2022-04-20 12:00:00", "2022-04-20 14:00:00", False),
        ("W14", "2022-04-20 07:00:00", "2022-04-20 09:00:00", False),
        ("W15", "2022-04-20 00:00:00", "2022-04-20 05:00:00", False),
        ("W16", "2022-04-20 21:00:00", "2022-04-20 23:00:00", False),
        ("W17", "2022-04-21 21:00:00", "2022-04-22 06:00:00", False),
        ("W18", "2022-04-24 00:00:00", "2022-04-24 23:59:59", False),
        ("W19", "2022-04-23 08:00:00", "2022-04-23 12:00:00", False)]


@pytest.fixture()
def scheduler() -> WorkoutScheduler:
    """ Returns  workout scheduler"""
    return WorkoutScheduler()


@pytest.mark.parametrize("wo_name,wo_start,wo_end, expected_validation", cases)
def test_workout_cases(scheduler, wo_name, wo_start, wo_end, expected_validation):
    workout = Workout(
        athlete_id=2,
        coach_id=10,
        name=wo_name,
        start_date_time=wo_start,
        end_date_time=wo_end
    )
    wo_validation, message = scheduler.plan_workout(workout=workout)
    assert wo_validation is expected_validation

