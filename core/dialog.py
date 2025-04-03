from core.ui import selector


def is_dialog_present(page):
    """Check if a dialog is present on the screen."""
    return page.locator(selector("dialog")).count()


def get_dialog_title(page):
    """Get the title of a dialog."""
    title = page.locator(selector("dialog-title"))
    return title.inner_text()


def get_dialog_text(page):
    """Get the text content of a dialog."""
    text = page.locator(selector("dialog-text"))
    return text.inner_text()


def click_dialog_button(page, button_type):
    """Click a specific dialog button."""
    button = page.locator(selector(button_type))
    if button.count() == 0:
        raise RuntimeError(f"Could not find button for {button_type}")
    button.click()
