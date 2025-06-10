from pushoverkit.message import Message

def setup_message_cli(subparsers):
    parser = subparsers.add_parser("message", help="Send a message")
    parser.add_argument("--token", required=True)
    parser.add_argument("--user", required=True)
    parser.add_argument("--message", required=True)
    parser.set_defaults(func=handle_message)

def handle_message(args):
    m = Message(token=args.token)
    res = m.send(user=args.user, message=args.message)
    print(res)