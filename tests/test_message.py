from config import token, user
from pushoverkit import Pushover

po = Pushover(token=token)
po.message.send()