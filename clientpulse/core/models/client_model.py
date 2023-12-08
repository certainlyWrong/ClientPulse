from datetime import datetime

from typing import Optional
from sqlmodel import Field, SQLModel


class ClientModel(SQLModel, table=True, schema="clientpulse"):
    id: Optional[int] = Field(
        default=None,
        primary_key=True,
    )
    name: str
    phone: Optional[str]
    email: Optional[str]
    address: Optional[str]
    description: Optional[str]
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime]
