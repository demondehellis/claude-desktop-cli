import os

def selector(button_type):
    selectors = {
        "new-chat": os.environ.get('CLAUDE_NEW_CHAT_BTN', '[aria-label="New chat"]'),
        "allow": os.environ.get('CLAUDE_ALLOW_ONCE_BTN', 'button:has-text("Allow Once")'),
        "allow-chat": os.environ.get('CLAUDE_ALLOW_CHAT_BTN', 'button:has-text("Allow for This Chat")'),
        "deny": os.environ.get('CLAUDE_DENY_BTN', 'button:has-text("Deny")'),
        "dialog": os.environ.get('CLAUDE_DIALOG_SELECTOR', '[role="dialog"]'),
        "dialog-title": os.environ.get('CLAUDE_DIALOG_TITLE_SELECTOR', '[role="dialog"] h2'),
        "dialog-text": os.environ.get('CLAUDE_DIALOG_TEXT_SELECTOR', '[role="dialog"] .flex-col>.text-xs'),
        "stop": os.environ.get('CLAUDE_STOP_BTN', '[aria-label="Stop Response"]'),
        "input": os.environ.get('CLAUDE_INPUT_SELECTOR', '.ProseMirror'),
        "response": os.environ.get('CLAUDE_RESPONSE_SELECTOR', '.group .font-claude-message>div:last-child'),
        "code-artifact": os.environ.get('CLAUDE_ARTIFACT_CODE_SELECTOR', '.min-h-full.prismjs'),
        "markdown-artifact": os.environ.get('CLAUDE_ARTIFACT_MARKDOWN_SELECTOR', '#markdown-artifact.font-claude-message'),
        "close-artifact": os.environ.get('CLAUDE_ARTIFACT_CLOSE_SELECTOR', '[d*="M205.66"]'),
        "open-artifact": os.environ.get('CLAUDE_ARTIFACT_OPEN_SELECTOR', '[d*="M5 10C5"]'),
        "preview-artifact": os.environ.get('CLAUDE_ARTIFACT_PREVIEW_SELECTOR', '.artifact-block-cell-preview'),
    }
    return selectors.get(button_type)
