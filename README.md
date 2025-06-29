# slack-mcp-client

A Python-based Slack bot integrating MCP functionality using LangChain and the OpenAI API.

The slack integration is implemented using the Slack Bolt API.

## Installation

> **Note:** This project requires **Python 3.11** or higher.

1. **Configure your Slack bot**  
   Set up a bot on Slack and ensure it has the necessary permissions.

2. **Set up the virtual environment**  
   Create and activate a virtual environment, then install dependencies using the `requirements.txt` file:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   Copy the `.env.example` file to `.env` and fill in the required values (e.g., Slack tokens, API keys).

4. **Add MCP server endpoints**
   Populate the `mcp-servers.json` file with your MCP server URLs. Make sure the servers are accessible and operational.

5. **Start the bot**
   Run the main script:
   ```bash
   python3 slack.py
   ```

6. **Interact via Slack**
   Send a message to your Slack bot to begin interacting with the MCP integration.
