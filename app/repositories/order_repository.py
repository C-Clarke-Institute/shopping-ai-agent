import select

from sqlalchemy.orm import Session

from app.models import Order


class OrderRepository:

    def __init__(self, session : Session):

        self.session= session

    def get_by_order_number(self, order_number : str) -> Order | None:

        statement = select(Order).where(Order.order_number == order_number)

        order = self.session.scalar(statement)

        return order