from .message import Message
from .group import Group
class Pushover:
    def __init__(self, token: str):
        self.token = token
        self.message = Message(self.token)
        self.group = Group(self.token)