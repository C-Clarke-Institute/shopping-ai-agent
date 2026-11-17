from langchain_core.tools import tool

from app.database.connection import SessionLocal
from app.repositories.order_repository import OrderRepository
from app.services.order_service import OrderService


@tool
def check_order_status(order_number : str):

    """
    Check the current status of a customer order.

    Use this tool when a customer asks about:
    - Order status
    - Order tracking
    - Estimated delivery
    - Order information

    Requires the customer's order number

    """
    
    with SessionLocal() as session :

        repository = OrderRepository(session)
        service = OrderService(repository)

        result = service.get_order_status(order_number.strip())

        return result