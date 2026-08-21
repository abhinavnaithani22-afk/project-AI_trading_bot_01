import logging

logger = logging.getLogger(__name__)

class BlofinAPIError(Exception):
    pass

class BlofinClient:
    def __init__(self, api_key=None, secret_key=None, passphrase=None, *args, **kwargs):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase
        logger.info("BlofinClient initialized.")

    def get_account_balance(self):
        return {"status": "success", "balance": 0.0}

    def place_order(self, *args, **kwargs):
        return {"status": "success", "order_id": "dummy_order_123"}

    def get_positions(self):
        return []

    def cancel_order(self, *args, **kwargs):
        return {"status": "success"}
