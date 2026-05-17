from dataclasses import dataclass
import uuid
from uuid import UUID

@dataclass
class UserRepository:

    name_user: str
    id_user: UUID = uuid.uuid4()



