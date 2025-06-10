import argparse
from .message_cli import setup_message_cli
from .group_cli import setup_group_cli

def main():
    parser = argparse.ArgumentParser(prog="pushoverkit")
    subparsers = parser.add_subparsers(dest="command", required=True)

    setup_message_cli(subparsers)
    setup_group_cli(subparsers)

    args = parser.parse_args()
    args.func(args)