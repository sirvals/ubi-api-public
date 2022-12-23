import json
import requests
from datetime import datetime

class Authorization:
    """
    A class for handling authorization with Ubisoft services.
    """
    def __init__(self):
        """
        Initialize the authorization object and perform the necessary authorization steps.
        """
        self.authed = self.twitch_authed = False
        datetime_now = datetime.now()
        time_now = datetime_now.strftime("%m/%d/%Y %H:%M:%S")
        print(f"Reauthorization @ {time_now}")
        if self.authed == False:
            self.auth()
        if self.twitch_authed == False:
            self.twitch_auth()

    def auth(self):
        """
        Perform authorization with Ubisoft services.
        """
        url = "https://public-ubiservices.ubi.com/v3/profiles/sessions"

        payload = json.dumps({"rememberMe": False})
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110  Safari/537.36",
            "GenomeId": "85c31714-0941-4876-a18d-2c7e9dce8d40",
            "Ubi-AppId": "314d4fef-e568-454a-ae06-43e3bece12a6",
            "Ubi-SessionId": "7710bcb4-b22e-49d2-8d20-402fc457f117",
            "Authorization": "Basic INCLUDEBASE64ENCODEDHERE",
            "Content-Type": "application/json"
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        response_json = json.loads(response.text)
        self.ticket = response_json["ticket"]
        self.expiration = response_json["expiration"]
        self.ip = response_json['clientIp']
        self.authed = True

    def twitch_auth(self):
        """
        Perform authorization with Ubisoft Twitch Endpoint.
        """
        url = "https://public-ubiservices.ubi.com/v3/profiles/sessions"

        payload = json.dumps({"rememberMe": False})
        headers = {
            "authorization": "Ubi_v1 t=" + self.ticket,
            "ubi-appid": "314d4fef-e568-454a-ae06-43e3bece12a6",
            "ubi-sessionid": "317cf60e-1e08-44b8-ad1e-d09c238c16ff",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
            "content-type": "application/json"
