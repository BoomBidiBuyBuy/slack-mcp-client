import os

from langfuse.callback import CallbackHandler


if os.environ.get("LANGFUSE_HOST", None) and \
    os.environ.get("LANGFUSE_PUBLIC_KEY", None) and \
    os.environ.get("LANGFUSE_SECRET_KEY", None):
    langfuse_handler = CallbackHandler(
        secret_key=os.environ.get("LANGFUSE_SECRET_KEY"),
        public_key=os.environ.get("LANGFUSE_PUBLIC_KEY"),
        host=os.environ.get("LANGFUSE_HOST")
    )
else:
    langfuse_handler = None
