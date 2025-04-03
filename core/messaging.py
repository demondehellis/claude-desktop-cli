import os
import sys
import time

from core.cli import print_dialog
from core.dialog import is_dialog_present, click_dialog_button
from core.ui import selector


def is_stop_button_present(page):
    """Check if the stop button is visible."""
    return page.locator(selector("stop")).count()


def start_new_chat(page):
    """Start a new chat by navigating to the new chat page."""
    button = page.locator(selector("new-chat"))
    button.press("Enter")

def send_message(page, message, delay=20):
    """Send a message to Claude."""
    textarea = page.locator(selector("input"))
    textarea.click()
    textarea.fill(message)
    textarea.press("Control+Enter")


def wait_until_ready(page, timeout=None, always_allow=False):
    """Wait for Claude to complete its response."""
    start_time = time.time()
    while True:
        # Check for dialogs during response
        if is_dialog_present(page):
            if always_allow:
                click_dialog_button(page, "allow-chat")
            else:
                print_dialog(page)
                sys.exit(0)

        if not is_stop_button_present(page):
            break

        if timeout and time.time() - start_time > timeout:
            raise TimeoutError("Timed out waiting {timeout} seconds for Claude to finish")

        # Wait a bit
        time.sleep(1)


def get_last_response(page):
    """Get Claude's response."""
    response_elements = page.locator(selector("response")).all()
    if response_elements:
        return response_elements[-1]
    else:
        return None
