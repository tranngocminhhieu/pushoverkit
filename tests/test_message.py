from config import token, user
from pushoverkit import Pushover

pushover = Pushover(token=token, default_user=user)
print(pushover.push(message='Hello World! Test from <a href="https://github.com/tranngocminhhieu/pushoverkit">PushoverKit</a>', title='Test title', monospace=1))