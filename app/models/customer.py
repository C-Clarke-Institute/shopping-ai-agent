from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.database.base import Base


class Customer(Base) :

    __tablename__ = "customers"

    id : Mapped[int] = mapped_column(primary_key=True, index=True)

    full_name : Mapped[str] = mapped_column(String(120), nullable=False)

    email: Mapped[str] = mapped_column(String(255), unique=True,
                                       index= True, nullable=False)

    phone: Mapped[str | None ] = mapped_column(String(20), nullable = True)

    created_at : Mapped[datetime] = mapped_column(DateTime,
                                                  default=datetime.utcnow(),
                                                  nullable=False
                                                  )
    orders : Mapped[list["Order"]] = relationship(back_populates="customer")