import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.integration_code = os.getenv("AUTOTASK_INTEGRATION_CODE")
        self.username = os.getenv("AUTOTASK_USERNAME")
        self.secret = os.getenv("AUTOTASK_SECRET")
        self.verbose = os.getenv("AUTOTASK_VERBOSE", "False").lower() == "true"
        self.debug = os.getenv("AUTOTASK_DEBUG", "False").lower() == "true" or self.verbose

    def validate(self):
        missing = []
        if not self.integration_code: missing.append("AUTOTASK_INTEGRATION_CODE")
        if not self.username: missing.append("AUTOTASK_USERNAME")
        if not self.secret: missing.append("AUTOTASK_SECRET")
        
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
        return True

config = Config()
