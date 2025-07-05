import os
import dotenv
import asyncio
import logging
import time

from agent import build_agent
from mcp_app import custom_mcp_servers, load_mcp_servers

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from langfuse_common import langfuse_handler


logging.basicConfig(level=logging.INFO)


# Initializes the bot client with your bot token
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
)


@app.message(".*")
def any_message_handler(message, say, context, logger):
    """
    This function is triggered for every message received by the Slack bot
    (matching the regular expression).

    The user's message is processed by an LLM agent implemented with LangChain,
    and the resulting response is sent back to the user.

    The agent communicates with the configured MCP services.
    """
    logger.info(f"Got the user message='{message}'")

    message_text = message.get("text")

    # The agent maintains conversation history per user_id using the context
    user_id = context["user_id"]

    # Instantiate a new agent for each incoming message to handle
    # messages independently and asynchronously
    # (note that conversation history will be lost, if you want to keep it
    # then you need to re-use an agent instance)
    agent = build_agent(custom_mcp_servers)

    callbacks = []
    if langfuse_handler:
        logger.info(f"Langfuse integration is set up")
        callbacks.append(langfuse_handler)
    else:
        logger.info(f"Langfuse integration is not set up")

    response = asyncio.run(
            agent.ainvoke(
                {"messages": [{"role": "user", "content": message_text}]},
                {
                    "callbacks": callbacks,
                    "configurable": {"thread_id": user_id}
                }
            )
    )

    # say respones back to the user
    say(
        text=response["messages"][-1].content
    )


def run_slack_app():
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
