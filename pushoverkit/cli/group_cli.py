from pushoverkit.group import Group

def setup_group_cli(subparsers):
    parser = subparsers.add_parser("group", help="Manage groups")
    group_subparsers = parser.add_subparsers(dest="group_command", required=True)

    create = group_subparsers.add_parser("create", help="Create a new group")
    create.add_argument("--token", required=True)
    create.add_argument("--name", required=True)
    create.add_argument("--users", default="")
    create.set_defaults(func=handle_create)

    add_user = group_subparsers.add_parser("add-user", help="Add user to group")
    add_user.add_argument("--token", required=True)
    add_user.add_argument("--group-key", required=True)
    add_user.add_argument("--user", required=True)
    add_user.set_defaults(func=handle_add_user)

def handle_create(args):
    g = Group(token=args.token)
    users = args.users.split(",") if args.users else []
    print(g.create(name=args.name, users=users))

def handle_add_user(args):
    g = Group(token=args.token)
    print(g.add_user(group_key=args.group_key, user=args.user))