import requests

class Message:
    def __init__(self, token: str):
        self.token = token
        self.default_user = None

    def send(self, message: str = "", user: str = None, title: str = None, **kwargs):
        user = user or self.default_user
        if not user:
            raise ValueError("User key is required (either as argument or default_user)")

        data = {
            "token": self.token,
            "user": user,
            "message": message
        }
        if title:
            data["title"] = title
        data.update(kwargs)

        response = requests.post("https://api.pushover.net/1/messages.json", data=data)
        response.raise_for_status()
        return response.json()