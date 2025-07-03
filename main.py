import dotenv
import threading

dotenv.load_dotenv()

from mcp_app import run_mcp_app
from slack_app import run_slack_app


# Start the app
if __name__ == "__main__":
    slack_thread = threading.Thread(target=run_slack_app, daemon=True)
    mcp_thread = threading.Thread(target=run_mcp_app, daemon=True)

    slack_thread.start()
    mcp_thread.start()

    threading.Event().wait()
