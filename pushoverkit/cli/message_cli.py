from pushoverkit import Pushover

def setup_message_cli(subparsers):
    parser = subparsers.add_parser("push", help="Push a message")
    parser.add_argument("--token", required=True)
    parser.add_argument("--user", required=True)
    parser.add_argument("--message", required=True)
    parser.set_defaults(func=handle_message)

def handle_message(args):
    p = Pushover(token=args.token, default_user=args.user)
    res = p.push(message=args.message)
    print(res)