# Slack MCP Server

A lightweight MCP server that bridges coding agent requests to a Slack channel for human-in-the-loop interactions.

## Prerequisites
- Python 3.10+
- A Slack App with:
  - `chat:write` scope
  - `SLACK_BOT_TOKEN`
  - `SLACK_SIGNING_SECRET`
  - `SLACK_CHANNEL_ID`

## Configuration
Create a `.env` file in the root directory:
```bash
SLACK_BOT_TOKEN=xoxb-...
SLACK_SIGNING_SECRET=...
SLACK_CHANNEL_ID=C...
```

## Running the Server
Install dependencies:
```bash
pip install -r requirements.txt
```

Run the server (uses `mcp` CLI or directly):
```bash
python server.py
```
