import requests
import base64
from requests.auth import HTTPBasicAuth
import time
import json
from .config import config

class AutotaskClient:
    DISCOVERY_URL = "https://webservices29.autotask.net/atservicesrest/v1.0/zoneInformation?user="

    def __init__(self):
        self.base_url = None
        self.integration_code = config.integration_code
        self.username = config.username
        self.secret = config.secret
        self.session = requests.Session()
        self.session.headers.update({
            "ApiIntegrationCode": self.integration_code,
            "UserName": self.username, 
            "Secret": self.secret,
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
        self.session.auth = HTTPBasicAuth(self.username, self.secret)

    def _log_request(self, prepped_request):
        if not config.debug:
            return
        
        print("\n" + "="*50)
        print(f"[*] --- HTTP REQUEST ---")
        print(f"[*] Method: {prepped_request.method}")
        print(f"[*] URL: {prepped_request.url}")
        
        # Redact sensitive headers
        headers = dict(prepped_request.headers)
        sensitive_headers = ["Secret", "Authorization"]
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
        print(f"[*] --- HTTP RESPONSE ---")
        print(f"[*] Status: {response.status_code}")
        
        if response.content:
            try:
                print(f"[*] Body: {json.dumps(response.json(), indent=2)}")
            except:
                print(f"[*] Body (Text): {response.text}")
        print("-"*50 + "\n")

    def _discover_zone(self):
        if config.verbose:
            print(f"[*] Discovering zone for user: {self.username}")
        
        url = f"{self.DISCOVERY_URL}{self.username}"
        req = requests.Request("GET", url)
        prepped = req.prepare()
        self._log_request(prepped)
        
        response = requests.get(url)
        self._log_response(response)
        
        response.raise_for_status()
        data = response.json()
        self.base_url = data.get("url")+'v1.0/'
        if not self.base_url:
            raise ValueError("Could not find zone URL in discovery response.")
        
        if config.verbose:
            print(f"[+] Using base URL: {self.base_url}")

    def request(self, method, endpoint, **kwargs):
        if not self.base_url:
            self._discover_zone()

        if endpoint.startswith("http"):
            url = endpoint
        else:
            url = f"{self.base_url}{endpoint.lstrip('/')}"
        
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
                    if "errors" in error_json:
                        error_msg = ", ".join(error_json["errors"])
                except:
                    pass
                
                print(f"[!] API Error ({response.status_code}): {error_msg}")
                raise e
            except Exception as e:
                print(f"[!] Request Error: {str(e)}")
                raise e
        
        raise Exception("Max retries exceeded.")

client = AutotaskClient()
