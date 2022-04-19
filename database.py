import uuid


class Database:
    # Asume that the database is a dictionary, all dates are already on UTC timezone
    data = {
        "workouts": [
            {"id": "83ffdd9a78ef4d7baa45e67e8845ece6", "athlete_id": 1, "coach_id": 10, "name": "wk_1",
             "start_date_time": "2022-04-19 07:00:00", "end_date_time": "2022-04-19 09:00:00"},
            
            {"id": "f0176fce57504ebdbe4a17e03fe9ee9a", "athlete_id": 1, "coach_id": 10, "name": "wk_2",
             "start_date_time": "2022-04-19 10:00:00", "end_date_time": "2022-04-19 12:00:00"},
            
            {"id": "85dac93ec4964e4abf17eb2368413727", "athlete_id": 1, "coach_id": 10, "name": "wk_3",
             "start_date_time": "2022-04-19 16:00:00", "end_date_time": "2022-04-19 18:00:00"}
        ],
        "coaches": {
            10: {"name": "Patrick Sang",
                 "unavailable_periods": {
                     "monday": [
                         {"start_time": "00:00:00", "end_time": "05:00:00"},
                         {"start_time": "22:00:00", "end_time": "23:59:59"}
                     ],
                     "tuesday": [
                         {"start_time": "00:00:00", "end_time": "05:00:00"},
                         {"start_time": "22:00:00", "end_time": "23:59:59"}
                     ],
                     "wednesday": [
                         {"start_time": "00:00:00", "end_time": "05:00:00"},
                         {"start_time": "22:00:00", "end_time": "23:59:59"}
                     ],
                     "thursday": [
                         {"start_time": "00:00:00", "end_time": "05:00:00"},
                         {"start_time": "22:00:00", "end_time": "23:59:59"}
                     ],
                     "friday": [
                         {"start_time": "00:00:00", "end_time": "05:00:00"},
                         {"start_time": "22:00:00", "end_time": "23:59:59"}
                     ],
                     "saturday": [
                         {"start_time": "00:00:00", "end_time": "05:00:00"},
                         {"start_time": "22:00:00", "end_time": "23:59:59"}
                     ],
                     "sunday": [
                         {"start_time": "00:00:00", "end_time": "05:00:00"},
                         {"start_time": "22:00:00", "end_time": "23:59:59"}
                     ]

                 }
                 },
            20: {"name": "Alberto Salazar",
                 "unavailable_periods": {
                     "tuesday": [
                         {"start_time": "00:00:00", "end_time": "05:00:00"},
                         {"start_time": "22:00:00", "end_time": "23:59:59"}
                     ]
                 }
                 }
        },
        "athletes": {
           1: {"name": "Eliud Kipchoge",
               "unavailable_periods": {
                   "monday": [],
                   "tuesday": [],
                   "wednesday": [],
                   "thursday": [],
                   "friday": [],
                   "saturday": [],
                   "sunday": []
                }
               },
           2: {"name": "Julian V",
               "unavailable_periods": {
                   "monday": [
                        {"start_time": "00:00:00", "end_time": "04:00:00"},
                        {"start_time": "08:00:00", "end_time": "13:00:00"},
                        {"start_time": "15:00:00", "end_time": "18:00:00"},
                        {"start_time": "22:00:00", "end_time": "23:59:59"}
                    ],
                   "tuesday": [
                        {"start_time": "00:00:00", "end_time": "04:00:00"},
                        {"start_time": "08:00:00", "end_time": "13:00:00"},
                        {"start_time": "15:00:00", "end_time": "18:00:00"},
                        {"start_time": "22:00:00", "end_time": "23:59:59"}
                   ],
                   "wednesday": [
                        {"start_time": "00:00:00", "end_time": "04:00:00"},
                        {"start_time": "08:00:00", "end_time": "13:00:00"},
                        {"start_time": "15:00:00", "end_time": "18:00:00"},
                        {"start_time": "22:00:00", "end_time": "23:59:59"}
                   ],
                   "thursday": [
                        {"start_time": "00:00:00", "end_time": "04:00:00"},
                        {"start_time": "08:00:00", "end_time": "13:00:00"},
                        {"start_time": "15:00:00", "end_time": "18:00:00"},
                        {"start_time": "22:00:00", "end_time": "23:59:59"}
                   ],
                   "friday": [
                        {"start_time": "00:00:00", "end_time": "04:00:00"},
                        {"start_time": "08:00:00", "end_time": "13:00:00"},
                        {"start_time": "15:00:00", "end_time": "18:00:00"},
                        {"start_time": "22:00:00", "end_time": "23:59:59"}
                   ],
                   "saturday": [
                        {"start_time": "00:00:00", "end_time": "04:00:00"},
                        {"start_time": "22:00:00", "end_time": "23:59:59"}
                   ],
                   "sunday": [
                       {"start_time": "00:00:00", "end_time": "04:00:00"},
                       {"start_time": "22:00:00", "end_time": "23:59:59"}
                   ]
               }
          }
        }
    }

    def get_coach_workouts(self, coach_id: int):
        return [wo for wo in self.data["workouts"] if wo["coach_id"] == coach_id]

    def get_athlete_workouts(self, athlete_id: int):
        return [wo for wo in self.data["workouts"] if wo["athlete_id"] == athlete_id]

    def get_coach_unavailable_periods(self, coach_id: int, day_mame: str):
        return self.data["coaches"][coach_id]["unavailable_periods"].get(day_mame, [])

    def get_athlete_unavailable_periods(self, athlete_id: int, day_mame: str):
        return self.data["athletes"][athlete_id]["unavailable_periods"].get(day_mame, [])

    def get_coach_by_id(self, coach_id: int):
        return self.data["coaches"].get(coach_id)

    def get_athlete_by_id(self, athlete_id: int):
        return self.data["athletes"].get(athlete_id)

    def insert_workout(self, workout: dict):
        workout.update({"id": uuid.uuid4().hex})
        self.data["workouts"].append(workout)
        return workout
