from bot.client import BinanceFuturesClient
from bot.validators import validate_order

class OrderEngine:
    def __init__(self):
        self.client = BinanceFuturesClient()

    def place_order(self, symbol, side, order_type, quantity, price=None):
        validate_order(symbol, side, order_type, quantity, price)

        order_params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            order_params["price"] = price
            order_params["timeInForce"] = "GTC"

        return self.client.create_order(order_params)
