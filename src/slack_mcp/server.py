import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from slack_mcp.slack_client import SlackClient

# Load environment variables from .env file
load_dotenv()

# Validate required configuration at startup
REQUIRED_ENV_VARS = ["SLACK_BOT_TOKEN", "SLACK_SIGNING_SECRET", "SLACK_CHANNEL_ID"]
for var in REQUIRED_ENV_VARS:
    if not os.environ.get(var):
        raise EnvironmentError(f"Missing required environment variable: {var}")

mcp = FastMCP("Slack-MCP-Server")
_slack_client = None

def get_slack_client():
    global _slack_client
    if _slack_client is None:
        _slack_client = SlackClient()
    return _slack_client

@mcp.tool()
def ask_slack(question: str) -> str:
    """Sends a question/approval request to the configured Slack channel."""
    if not question.strip():
        return "Error: Cannot send an empty message."

    channel_id = os.environ.get("SLACK_CHANNEL_ID")
    
    try:
        get_slack_client().send_message(channel_id, question)
        return "Message sent to Slack successfully."
    except Exception:
        # Log the specific error internally in a real application
        return "Error: Failed to send message to Slack. Please check configuration."

if __name__ == "__main__":
    mcp.run()
