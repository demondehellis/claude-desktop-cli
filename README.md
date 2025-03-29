# Claude Desktop CLI

A Python-based command-line tool to programmatically control the Claude desktop app using Playwright.

## Overview

Claude Controller is a utility that allows you to interact with the Claude AI desktop application programmatically. It uses Playwright to connect to the app via Chrome DevTools Protocol and enables you to:

- Start new chats
- Send messages
- Retrieve responses
- Handle dialogs (allow or deny actions)
- Extract artifacts created by Claude (code or markdown)

This tool is useful for automating interactions with Claude, integrating Claude into other workflows, or creating custom interfaces on top of the Claude desktop app.

## Installation

### Prerequisites

- Python 3.11+
- Claude desktop app installed and running in debug mode:

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/demondehellis/claude-desktop-cli.git
   cd claude-desktop-cli
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Playwright browsers:
   ```bash
   python -m playwright install
   ```

5. Create a `.env` file from the example:
   ```bash
   cp .env.example .env
   ```

## Running Claude in Debug Mode

To use this tool, Claude must be running in debug mode:

### macOS
```bash
/Applications/Claude.app/Contents/MacOS/Claude --remote-debugging-port=9333
```

### Windows
```bash
"C:\Path\To\Claude.exe" --remote-debugging-port=9333
```

## Usage

The tool provides several command-line options:

```bash
python main.py [OPTIONS]
```

### Basic Options

- `--port PORT`: Debug port (default: from CLAUDE_DEBUG_PORT or 9333)
- `--message "Your message"`: Send a message to Claude
- `--new-chat`: Start a new chat
- `--timeout SECONDS`: Timeout in seconds for response

### Dialog Handling

- `--dialog-action [allow|allow-chat|deny]`: Action to take on dialog
- `--always-allow`: Always allow running actions without asking

### Artifact Handling

- `--get-artifact`: Get the content of the artifact panel

## Examples

### Start a new chat and send a message

```bash
python main.py --new-chat --message "Hello, Claude! How are you today?"
```

### Send a message to an existing chat

```bash
python main.py --message "Can you help me with a Python script?"
```

### Get an artifact (when Claude has created one)

```bash
python main.py --get-artifact
```

### Deal with dialogs automatically

```bash
python main.py --message "Run ls -la" --always-allow
```

## Environment Variables

You can configure the tool by setting environment variables in your `.env` file:

- `CLAUDE_DEBUG_PORT`: Debug port to connect to (default: 9333)
- `CLAUDE_TIMEOUT`: Default timeout for responses in seconds
- `CLAUDE_SLOW_MO`: Slow down Playwright operations (in ms, default: 900)

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.