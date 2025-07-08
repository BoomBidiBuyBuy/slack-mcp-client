# slack-mcp-client

A Python-based Slack bot integrating MCP functionality using LangChain and the OpenAI API.
The slack client also contains it's own MCP server that allows to add other MCP endpoints dynamically

The slack integration is implemented using the Slack Bolt API.

## Installation

> **Note:** This project requires **Python 3.12** or higher.

1. **Configure your Slack bot**  
   Set up a bot on Slack and ensure it has the necessary permissions.

2. **Set your environment**  
   Set up your environment using the `uv` tool
   ```bash
   uv sync
   ```

3. **Configure environment variables**
   Copy the `.env.example` file to `.env` and fill in the required values (e.g., Slack tokens, API keys).

4. **Add MCP server endpoints**
   Populate the `mcp-servers.json` file with your MCP server URLs. Make sure the servers are accessible and operational.

5. **Start the bot**
   Run the main script:
   ```bash
   uv run main.py
   ```

6. **Interact via Slack**
   Send a message to your Slack bot to begin interacting with the MCP integration.
