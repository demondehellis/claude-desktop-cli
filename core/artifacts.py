from core.ui import selector


def is_code_artifact_present(page):
    """Check if the code artifact is present on the screen."""
    return page.locator(selector("code-artifact")).count()


def is_markdown_artifact_present(page):
    """Check if the markdown artifact is present on the screen."""
    return page.locator(selector("markdown-artifact")).count()


def close_artifact_panel(page):
    """Click a specific dialog button."""
    button = page.locator(selector("close-artifact"))
    try:
        button.click()
    except Exception as e:
        print(f"Error closing artifact panel: {e}")


def get_code_artifact(page):
    """Get the code from the artifact panel."""
    code = page.locator(selector("code-artifact"))
    if code.count() == 0:
        raise RuntimeError(f"Could not find code artifact")

    return code.inner_text()


def get_markdown_artifact(page):
    """Get the markdown from the artifact panel."""
    artifact = page.locator(selector("markdown-artifact"))
    if artifact.count() == 0:
        raise RuntimeError(f"Could not find markdown artifact")

    return html_to_md(artifact.inner_html())


def html_to_md(html):
    import html2text
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    markdown = h.handle(html)
    return markdown


def get_artifact(page):
    """Get the artifact from the artifact panel."""
    if is_code_artifact_present(page):
        return get_code_artifact(page)
    elif is_markdown_artifact_present(page):
        return get_markdown_artifact(page)
    else:
        raise RuntimeError(f"Could not find artifact")


def has_artifact_preview(element):
    """Check if the artifact preview button is present."""
    return element.locator(selector("preview-artifact")).count() > 0