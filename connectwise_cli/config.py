import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.company_id = os.getenv("CONNECTWISE_COMPANY_ID")
        self.public_key = os.getenv("CONNECTWISE_PUBLIC_KEY")
        self.private_key = os.getenv("CONNECTWISE_PRIVATE_KEY")
        self.client_id = os.getenv("CONNECTWISE_CLIENT_ID")
        self.basic_auth_key = os.getenv("CONNECTWISE_BASIC_AUTH_KEY")
        self.base_url = os.getenv("CONNECTWISE_API_URL")
        self.verbose = os.getenv("CONNECTWISE_VERBOSE", "False").lower() == "true"
        self.debug = os.getenv("CONNECTWISE_DEBUG", "False").lower() == "true" or self.verbose

    def validate(self):
        missing = []
        if not self.company_id: missing.append("CONNECTWISE_COMPANY_ID")
        if not self.public_key: missing.append("CONNECTWISE_PUBLIC_KEY")
        if not self.private_key: missing.append("CONNECTWISE_PRIVATE_KEY")
        if not self.client_id: missing.append("CONNECTWISE_CLIENT_ID")
        if not self.base_url: missing.append("CONNECTWISE_API_URL")
        
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
        return True

config = Config()
