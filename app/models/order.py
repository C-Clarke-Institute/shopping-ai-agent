from datetime import datetime
from decimal import Decimal

from sqlalchemy import String, ForeignKey, DECIMAL, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Order(Base) :

    __tablename__ = "orders"

    id : Mapped[int] = mapped_column(primary_key=True, index=True)

    order_number : Mapped[str] = mapped_column(String(30),unique=True,index=True,
                                               nullable=False)
    customer_id : Mapped[int] = mapped_column(
        ForeignKey("customers.id"), nullable=False
    )

    status: Mapped[str] = mapped_column(String(30), nullable=False,default="PROCESSING")

    total_amount : Mapped[Decimal] = mapped_column(Numeric(10,2),nullable=False)

    created_at : Mapped[datetime] = mapped_column(DateTime, nullable=False)

    estimated_delivery: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    customer: Mapped["Customer"] = relationship(back_populates="orders")
