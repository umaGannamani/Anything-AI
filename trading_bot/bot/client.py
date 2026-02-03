import os
import logging
from binance.client import Client
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
load_dotenv()

class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise EnvironmentError("API keys not found in environment variables")

        self.client = Client(api_key, api_secret, testnet=True)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        logger.info("Binance Futures Testnet client initialized")

    def create_order(self, params: dict):
        try:
            logger.info(f"SENT REQUEST: {params}")
            response = self.client.futures_create_order(**params)
            logger.info(f"RECEIVED RESPONSE: {response}")
            return response
        except Exception as e:
            logger.error(f"API ERROR: {e}", exc_info=True)
            raise
