import os

import requests
from playwright.sync_api import sync_playwright


def get_debug_targets(debug_port):
    """Get available debug targets from Chrome DevTools Protocol."""
    try:
        response = requests.get(f"http://localhost:{debug_port}/json/list")
        if response.status_code != 200:
            print(f"Error: Could not connect to debugging port {debug_port}")
            return None

        targets = response.json()
        return targets

    except requests.exceptions.ConnectionError:
        print(f"Could not connect to debug port {debug_port}")
        return None
    except Exception as e:
        print(f"Error getting debug targets: {str(e)}")
        return None


def setup_connection(debug_port, slow_mo=900, timeout=5000):
    """Initialize Playwright and connect to the browser."""
    try:
        playwright = sync_playwright().start()
        browser = playwright.chromium.connect_over_cdp(
            f"http://localhost:{debug_port}",
            slow_mo=slow_mo,
            timeout=timeout
        )
        return playwright, browser
    except Exception as e:
        print(f"Error connecting with Playwright: {str(e)}")
        return None, None


def find_claude_page(browser):
    """Find the Claude page among all browser contexts and pages."""
    try:
        for context in browser.contexts:
            for page in context.pages:
                url = page.url
                if 'claude.ai/chat' in url or 'claude.ai/new' in url:
                    return page

        print("Could not find any Claude page in any context")
        return None

    except Exception as e:
        print(f"Error finding Claude page: {str(e)}")
        return None


def connect_to_claude(debug_port=None):
    """Connect to the Claude app and return the page, browser, and playwright."""
    slow_mo = int(os.environ.get('CLAUDE_SLOW_MO', 900))
    timeout = int(os.environ.get('CLAUDE_DEFAULT_TIMEOUT', 5000))
    port = int(debug_port or os.environ.get('CLAUDE_DEBUG_PORT', 9333))

    targets = get_debug_targets(port)
    if targets is None:
        return None, None, None

    playwright, browser = setup_connection(port, slow_mo, timeout)
    if playwright is None or browser is None:
        return None, None, None

    page = find_claude_page(browser)
    if page is None:
        browser.close()
        playwright.stop()
        return None, None, None

    return page, browser, playwright


def close_connection(browser, playwright):
    """Close the connection to Claude app."""
    if browser:
        try:
            browser.close()
        except Exception as e:
            print(f"Error closing browser: {str(e)}")

    if playwright:
        try:
            playwright.stop()
        except Exception as e:
            print(f"Error stopping Playwright: {str(e)}")
