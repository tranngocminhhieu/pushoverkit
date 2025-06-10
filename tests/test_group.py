from pushoverkit import Pushover
from config import token, user
po = Pushover(token=token)

new_group = po.group.create(name='New Group')

rename = po.group.rename(group_key=new_group['group'], name='My Group')

add_user = po.group.add_user(group_key=new_group['group'], user=user)

disable_user = po.group.disable_user(group_key=new_group['group'], user=user)

enable_user = po.group.enable_user(group_key=new_group['group'], user=user)

list_users = po.group.list_users(group_key=new_group['group'])

remove_user = po.group.remove_user(group_key=new_group['group'], user=user)

list_groups = po.group.list_groups()