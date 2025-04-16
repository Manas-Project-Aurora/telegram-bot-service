from enum import StrEnum


class VacancyType(StrEnum):
    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    INTERNSHIP = "internship"
    REMOTE = "remote"
    PROJECT_BASED = "project_based"
