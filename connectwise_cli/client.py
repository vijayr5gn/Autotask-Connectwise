import requests
import base64
from requests.auth import HTTPBasicAuth
import time
import json
from .config import config

class ConnectWiseClient:
    def __init__(self):
        self.base_url = config.base_url
        self.company_id = config.company_id
        self.public_key = config.public_key
        self.private_key = config.private_key
        self.client_id = config.client_id
        self.basic_auth_key = config.basic_auth_key
        self.session = requests.Session()
        
        # ConnectWise Auth: Basic {Base64(companyid+publickey:privatekey)}
        # Generate the auth key dynamically to avoid stale/mismatched hardcoded values
        if self.basic_auth_key:
            auth_token = self.basic_auth_key
        else:
            # Build it from the individual credentials
            credentials = f"{self.company_id}+{self.public_key}:{self.private_key}"
            auth_token = base64.b64encode(credentials.encode()).decode()
        
        # Always regenerate from credentials to ensure correctness
        credentials = f"{self.company_id}+{self.public_key}:{self.private_key}"
        auth_token = base64.b64encode(credentials.encode()).decode()
        
        self.session.headers.update({
            "clientId": self.client_id,
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Basic {auth_token}"
        })

    def _log_request(self, prepped_request):
        if not config.debug:
            return
        
        print("\n" + "="*50)
        print(f"[*] --- CONNECTWISE REQUEST ---")
        print(f"[*] Method: {prepped_request.method}")
        print(f"[*] URL: {prepped_request.url}")
        
        # Redact sensitive headers
        headers = dict(prepped_request.headers)
        sensitive_headers = ["Authorization"]
        for h in sensitive_headers:
            if h in headers:
                headers[h] = "********"
        
        print(f"[*] Headers: {json.dumps(headers, indent=2)}")
        if prepped_request.body:
            body = prepped_request.body
            if isinstance(body, bytes):
                try:
                    body = body.decode('utf-8')
                    # Try to format as JSON for readability
                    try:
                        body_json = json.loads(body)
                        body = json.dumps(body_json, indent=2)
                    except:
                        pass
                except:
                    body = str(body)
            print(f"[*] Body: {body}")
        print("="*50 + "\n")

    def _log_response(self, response):
        if not config.debug:
            return
        
        print("\n" + "-"*50)
        print(f"[*] --- CONNECTWISE RESPONSE ---")
        print(f"[*] Status: {response.status_code}")
        
        if response.content:
            try:
                print(f"[*] Body: {json.dumps(response.json(), indent=2)}")
            except:
                print(f"[*] Body (Text): {response.text}")
        print("-"*50 + "\n")

    def request(self, method, endpoint, **kwargs):
        if not self.base_url:
             raise ValueError("ConnectWise API URL is not configured.")

        # Ensure base URL ends with / and endpoint doesn't start with /
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        
        # Prepare request to capture all headers and final URL for logging
        req = requests.Request(method, url, **kwargs)
        prepped = self.session.prepare_request(req)
        self._log_request(prepped)

        retries = 3
        backoff = 1
        for attempt in range(retries):
            try:
                response = self.session.send(prepped)
                self._log_response(response)
                
                if response.status_code == 429: # Rate limit
                    time.sleep(backoff)
                    backoff *= 2
                    continue
                
                response.raise_for_status()
                return response.json() if response.content else {}
            
            except requests.exceptions.HTTPError as e:
                if response.status_code >= 500:
                    time.sleep(backoff)
                    backoff *= 2
                    continue
                
                # Print API-specific error messages if available
                error_msg = response.text
                try:
                    error_json = response.json()
                    if "message" in error_json:
                        error_msg = error_json["message"]
                    elif isinstance(error_json, list) and len(error_json) > 0 and "message" in error_json[0]:
                        error_msg = error_json[0]["message"]
                except:
                    pass
                
                print(f"[!] ConnectWise API Error ({response.status_code}): {error_msg}")
                raise e
            except Exception as e:
                print(f"[!] Request Error: {str(e)}")
                raise e
        
        raise Exception("Max retries exceeded.")

client = ConnectWiseClient()
