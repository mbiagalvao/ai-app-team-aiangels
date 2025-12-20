"""
Tracing Configuration - Langfuse setup

Initialize observability for the entire application.
Call init_tracing() once at app startup.
"""

import os
from dotenv import load_dotenv


def init_tracing():
    """Initialize Langfuse tracing.

    This function should be called once at application startup.
    It loads environment variables and verifies Langfuse configuration.

    Langfuse automatically reads from these environment variables:
    - LANGFUSE_PUBLIC_KEY
    - LANGFUSE_SECRET_KEY
    - LANGFUSE_HOST

    Once initialized, all @observe() decorators will work automatically.
    """
    load_dotenv()

    # Check if Langfuse is configured
    required_keys = [
        "LANGFUSE_PUBLIC_KEY",
        "LANGFUSE_SECRET_KEY",
        "LANGFUSE_HOST"
    ]

    missing = [key for key in required_keys if not os.getenv(key)]

    if missing:
        print(f"⚠️  Langfuse not configured. Missing: {missing}")
        print("    Tracing will be disabled.")
        print("    Add keys to .env file to enable tracing.")
        return False
    else:
        print("✅ Langfuse tracing enabled")
        print(f"   Host: {os.getenv('LANGFUSE_HOST')}")
        return True


def get_trace_url(trace_id: str) -> str:
    """Get URL to view a specific trace in Langfuse.

    Args:
        trace_id: Langfuse trace ID

    Returns:
        URL to trace in Langfuse dashboard
    """
    host = os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")
    return f"{host}/trace/{trace_id}"
