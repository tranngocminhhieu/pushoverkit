# PushoverKit
**The powerful, Pythonic way to send Pushover notifications — from code or from the command line.**

PushoverKit is a lightweight, intuitive wrapper around the [Pushover API](https://pushover.net/api). It supports **sending messages**, **managing groups**, and comes with a handy **CLI** for quick scripting or automation.

## 📦 Installation

Install directly from GitHub (latest version):
```shell
pip install git+https://github.com/tranngocminhhieu/pushoverkit.git
```

Or from PyPI (when available):
```shell
pip install pushoverkit
```

## 🐍 Python Usage
```python
from pushoverkit import Pushover

pushover = Pushover(token='YOUR_TOKEN', default_user='YOUR_USER/GROUP_KEY')
```

**Required:**
- `token`: Your Pushover app token.

**Optional:**
- `default_user`: Default user key to send the message to.


### 📨 Push a Message
```python
pushover.push(message='Hello World!', title='PushoverKit', attachment='image.png') # Use default_user
```

**Required:**
- `message`: Message content.

**Optional:**
- `user`: User key to send the message to.
- `title`: Message title.
- `device`: Target a specific device.
- `html`: Enable HTML formatting (1 or 0), default to `0`.
- `monospace`: Enable monospace font (1 or 0), default to `0`.
- `priority`: Message priority, default to `0`, valid values in `[-2, -1, 0, 1, 2]`.
- `sound`: Override default notification sound.
- `timestamp`: Unix timestamp for the message.
- `ttl`: Time to live for emergency-priority messages.
- `url`: Supplementary URL to include.
- `url_title`: Title for the supplementary URL.
- `attachment`: Path to a file to attach.
- `attachment_base64`: Base64-encoded attachment data.
- `attachment_type`: MIME type for the base64 attachment.

### 👥 Manage Groups
```python
# Create a group
pushover.Groups.create(name="My Team")

# Add a user
pushover.Groups.add_user(group_key="GROUP_KEY", user="USER_KEY", memo="New teammate")

# And more methods
```

**Methods:**
- `create`: Create a new group.
- `rename`: Rename a group.
- `list_groups`: List all groups.
- `list_users`: List users in a group.
- `add_user`: Add user to group.
- `remove_user`: Remove user from group.
- `disable_user`: Disable user in group.
- `enable_user`: Enable user in group.

**Required:**
- `name`: Name of the group.
- `group_key`: Your group key.
- `user`: User key.

**Optional:**
- `device`: Target a specific device.
- `memo`: User Name or Memo.

## 🧰 CLI Usage
PushoverKit includes a built-in CLI for shell lovers and automation fans.

```shell
# Push a notification
pushoverkit push --token YOUR_TOKEN --user USER_KEY --message "Hello World!" --title "PushoverKit" --attachment "image.png"

# Create a group
pushoverkit groups create --token YOUR_TOKEN --name "My Group"

# Add a user to the group
pushoverkit groups add-user --token YOUR_TOKEN --group-key GROUP_KEY --user USER_KEY --memo "New teammate"

pushoverkit teams add-user --

# And more commands
```
### ℹ️ CLI Help
Each command comes with full help:
```shell
pushoverkit push --help
pushoverkit groups --help
pushoverkit groups create --help

# And more
```

## ❤️ Why PushoverKit?
-  Clean, Pythonic interface.
-  Full support for Pushover Message + Group APIs.
-  Includes a modern CLI.
-  No extra dependencies — just requests.