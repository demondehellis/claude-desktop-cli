import argparse
import os

from core.artifacts import has_artifact_preview, html_to_md
from core.dialog import get_dialog_text, get_dialog_title
from core.ui import selector


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Minimalistic Claude app controller")

    # Connection settings
    parser.add_argument("--port", type=int, help="Debug port (default: from CLAUDE_DEBUG_PORT or 9333)")

    # Action to perform
    parser.add_argument("--message", type=str, help="Message to send to Claude")
    parser.add_argument("--new-chat", action="store_true", help="Start a new chat")

    # Dialog handling
    parser.add_argument("--dialog-action", choices=["allow", "allow-chat", "deny"],
        help="Action to take on dialog (allow, allow-chat, or deny)"
    )
    parser.add_argument("--always-allow", action="store_true",
        help="Always allow running actions without asking"
    )

    # Artifact handling
    parser.add_argument("--get-artifact", action="store_true",
        help="Get the content of the artifact panel"
    )

    # Delay settings
    parser.add_argument("--delay", type=int, default=20,
        help="Delay in milliseconds for typing (default: 20)"
    )

    # Response handling
    parser.add_argument("--timeout", type=int,
        help="Timeout in seconds for response (use 0 to disable waiting)"
    )

    return parser.parse_args()

def print_dialog(page):
    title = get_dialog_title(page)
    text = get_dialog_text(page)
    print(f"\n(DIALOG POPUP)  {title}\n\n{text}\n")

    print("\nUse --dialog-action option with one of these values: allow, allow-chat, deny")

def print_artifact_preview(artifact):
    print(
        f"= = =(ARTIFACT PREVIEW)= = =\n"
        f"{artifact.inner_text()}\n\n"
        f"= = = = = = = = = = = = = = = =\n"
        f"(OPTIONS) Use --get-artifact to get the content if needed.")

def print_response(response):
    html = response.inner_html()

    # Cut out the artifact preview button
    artifact = response.locator(selector("preview-artifact"))
    if artifact.count():
        html = html.replace(artifact.inner_html(), "")

    print(html_to_md(html))
    if artifact.count():
        print_artifact_preview(artifact)
