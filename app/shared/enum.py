import enum


class CompanyMode(enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class TaskStatus(enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class TaskPriority(enum.Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"