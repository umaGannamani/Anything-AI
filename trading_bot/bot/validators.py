# validators.py

def validate_order(symbol, side, order_type, quantity, price=None):
    """
    Validates basic order parameters before sending to Binance Futures API
    """

    # Symbol validation
    if not isinstance(symbol, str):
        raise ValueError("Symbol must be a string")

    if not symbol.isupper():
        raise ValueError("Symbol must be uppercase (e.g., BTCUSDT)")

    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT-M futures pairs are supported")

    # Side validation
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    # Order type validation
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    # Quantity validation
    if quantity is None or quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    # Price validation for LIMIT orders
    if order_type == "LIMIT":
        if price is None or price <= 0:
            raise ValueError("Valid price is required for LIMIT orders")

    return True


def validate_notional(quantity, price, min_notional=100):
    """
    Ensures order value meets minimum notional requirement (USDT)
    Binance Futures Testnet commonly requires ~100 USDT minimum
    """

    if price is None:
        # MARKET orders may not have price at validation time
        return True

    notional = quantity * price

    if notional < min_notional:
        raise ValueError(
            f"Order value must be at least {min_notional} USDT "
            f"(current: {notional:.2f} USDT)"
        )

    return True
