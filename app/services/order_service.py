from app.repositories.order_repository import OrderRepository


class OrderService:

    def __init__(self, order_repository : OrderRepository):

        self.order_repository = order_repository

    def get_order_status(self,order_number : str):


        #retrieve order from repository
        order = self.order_repository.get_by_order_number(order_number)


        #check  wheteher order exists
        if order is None:
            return {"success" : False,
                    "message" : "Order not found"}

        order_data = {
            "order_number" : order.order_number,
            "status" : order.status,
            "total_amount" : order.total_amount,
            "created_at" : order.created_at.isoformat(),
            "estimated_delivery" : (
                order.estimated_delivery.isoformat() if order.estimated_delivery else None
            )
         }

        return {
            "success" : True,
            "message" : "Order retrieved successfully",
            "data" : order_data
        }
