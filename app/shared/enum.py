import enum


class CompanyMode(enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class TaskStatus(enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class TaskPriority(enum.Enum):
    HIGHEST = "HIGHEST"
    MEDIUM = "MEDIUM"
    LOW = "LOW"