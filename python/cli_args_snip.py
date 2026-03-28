"""A snippet that used CLI arguments.

Usage:
- python -B cli_args_snip.py -u <username>
- python -B cli_args_snip.py -h
"""
import argparse
from typing import Optional

def say_hello(username: Optional[str] = None) -> None:
    """Print a greeting to STDOUT.

    :param Optional[str] username: The user to greet, defaults to None.
    """
    # Account for no argument
    username = 'World' if username is None else username

    print(f"Hello, {username}!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='python -B cli_args_snip.py',
        description='A snippet that uses CLI arguments.'
    )
    parser.add_argument('-u', '--username', type=str, default=None,
                        help="The user to greet, defaults to 'World' if not provided.")
    args = parser.parse_args()

    say_hello(args.username)
