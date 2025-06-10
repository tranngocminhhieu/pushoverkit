import argparse
from pushoverkit.message import Message
from pushoverkit.group import Group

def main():
    parser = argparse.ArgumentParser(prog="pushoverkit")
    subparsers = parser.add_subparsers(dest="command")

    # MESSAGE
    msg_parser = subparsers.add_parser("message", help="Send a Pushover message")
    msg_parser.add_argument("--token", required=True)
    msg_parser.add_argument("--user", required=True)
    msg_parser.add_argument("--message", required=True)

    # GROUP
    group_parser = subparsers.add_parser("group", help="Group management")
    group_subparsers = group_parser.add_subparsers(dest="group_command", required=True)

    # group create
    create_parser = group_subparsers.add_parser("create")
    create_parser.add_argument("--token", required=True)
    create_parser.add_argument("--name", required=True)
    create_parser.add_argument("--users", help="Comma-separated user keys")

    # group rename
    rename_parser = group_subparsers.add_parser("rename")
    rename_parser.add_argument("--token", required=True)
    rename_parser.add_argument("--group-key", required=True)
    rename_parser.add_argument("--name", required=True)

    # group add-user
    add_user_parser = group_subparsers.add_parser("add-user")
    add_user_parser.add_argument("--token", required=True)
    add_user_parser.add_argument("--group-key", required=True)
    add_user_parser.add_argument("--user", required=True)

    # ...

    args = parser.parse_args()

    if args.command == "message":
        m = Message(token=args.token)
        res = m.send(user=args.user, message=args.message)
        print(res)

    elif args.command == "group":
        g = Group(token=args.token)

        if args.group_command == "create":
            users = args.users.split(",") if args.users else []
            res = g.create(name=args.name, users=users)
            print(res)

        elif args.group_command == "rename":
            res = g.rename(group_key=args.group_key, name=args.name)
            print(res)

        elif args.group_command == "add-user":
            res = g.add_user(group_key=args.group_key, user=args.user)
            print(res)

        # ...

if __name__ == "__main__":
    main()