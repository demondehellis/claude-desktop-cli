#!/usr/bin/env python3
import sys

from dotenv import load_dotenv

from core.artifacts import get_artifact
from core.cli import parse_arguments, print_response
from core.dialog import click_dialog_button

# Load environment variables from .env file if it exists
load_dotenv()

from core.connection import connect_to_claude, close_connection
from core.messaging import start_new_chat, send_message, get_last_response, wait_until_ready


def main():
    """Main function to run the CLI."""
    args = parse_arguments()

    # Connect to Claude
    page, browser, playwright = connect_to_claude(args.port)
    if not page:
        print("Failed to connect to Claude app")
        sys.exit(1)

    try:
        # Start a new chat if requested
        if args.new_chat:
            start_new_chat(page)

        # Handle dialog if present
        if args.dialog_action:
            click_dialog_button(page, args.dialog_action)

        # Handle ongoing conversations
        wait_until_ready(page, args.timeout)

        # Handle Artifact if present
        if args.get_artifact:
            print(get_artifact(page))
            sys.exit(0)

        # Send message if provided
        if args.message:
            send_message(page, args.message, args.delay)

        # Wait for Claude to finish processing
        wait_until_ready(page, args.timeout, args.always_allow)

        # By default, get last response
        response = get_last_response(page)
        if response:
            print_response(response)
            sys.exit(0)

        print("No response yet")
        sys.exit(1)

    except KeyboardInterrupt:
        print("\nOperation interrupted by user")
    finally:
        close_connection(browser, playwright)


if __name__ == "__main__":
    main()
