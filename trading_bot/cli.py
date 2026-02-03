import argparse
import logging
from bot.orders import OrderEngine
from bot.logging_config import setup_logging

setup_logging()
logger = logging.getLogger("CLI")

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot (Testnet)")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    engine = OrderEngine()

    try:
        response = engine.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\n✅ ORDER SUCCESS")
        print(f"Order ID     : {response.get('orderId')}")
        print(f"Status       : {response.get('status')}")
        print(f"Executed Qty : {response.get('executedQty')}")
        print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")

    except Exception as e:
        logger.error("Order execution failed")
        print(f"\n❌ ORDER FAILED: {e}")

if __name__ == "__main__":
    main()
