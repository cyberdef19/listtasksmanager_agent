from dataclasses import dataclass
import uuid
from uuid import UUID

@dataclass
class TaskRepository:

    name_task: str
    id_task: UUID = uuid.uuid4()