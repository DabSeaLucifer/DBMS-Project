from enum import Enum

class gender(Enum):
    male = 0
    female = 1

class seeker_status(Enum):
    employed = 0
    searching = 1
    non_working = 2

class job_status(Enum):
    vacant = 0
    filled = 1
    discontinued = 2

class job_type(Enum):
    remote_part_time = 0
    onsite_part_time = 1
    remote_full_time = 2
    onsite_full_time = 3