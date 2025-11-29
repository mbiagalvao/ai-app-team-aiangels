"""
utils.py - Utility functions for the AI chatbot application.
It includes tracing and prompt initialization functions.
"""

import os
from dotenv import load_dotenv
from pathlib import Path


def init_tracing():
    """
    Initialize Langfuse tracing.

    Langfuse uses environment variables automatically:
    - LANGFUSE_PUBLIC_KEY
    - LANGFUSE_SECRET_KEY
    - LANGFUSE_HOST

    If these are set in .env, tracing will be enabled.
    If not, the app will still work but without tracing.
    """
    load_dotenv()

    required = [
        "LANGFUSE_PUBLIC_KEY",
        "LANGFUSE_SECRET_KEY",
        "LANGFUSE_HOST"
    ]

    missing = [key for key in required if not os.getenv(key)]

    if missing:
        print("⚠️  Langfuse tracing not configured")
        print(f"   Missing: {', '.join(missing)}")
        print("   App will run without tracing")
        return False
    else:
        print("✅ Langfuse tracing enabled")
        print(f"   Host: {os.getenv('LANGFUSE_HOST')}")
        return True


class PromptLoader:
    """Load and manage prompt templates from files."""

    def __init__(self, prompts_dir: str = None):
        """
        Initialize prompt loader.

        Args:
            prompts_dir: Path to prompts directory (defaults to ../prompts)
        """
        if prompts_dir is None:
            # Get the directory where this file is located
            current_dir = Path(__file__).parent
            # Go up one level and into prompts/
            prompts_dir = current_dir.parent / "prompts"

        self.prompts_dir = Path(prompts_dir)

    def load(self, prompt_name: str) -> str:
        """
        Load a prompt template from file.

        Args:
            prompt_name: Name of prompt file (without .txt extension)

        Returns:
            Prompt template string

        Example:
            >>> loader = PromptLoader()
            >>> prompt = loader.load("classify_ticket")
        """
        prompt_path = self.prompts_dir / f"{prompt_name}.txt"

        if not prompt_path.exists():
            raise FileNotFoundError(f"Prompt file not found: {prompt_path}")

        with open(prompt_path, 'r', encoding='utf-8') as f:
            return f.read()

    def format(self, prompt_name: str, **kwargs) -> str:
        """
        Load and format a prompt template with variables.

        Args:
            prompt_name: Name of prompt file
            **kwargs: Variables to substitute in template

        Returns:
            Formatted prompt string

        Example:
            >>> loader = PromptLoader()
            >>> prompt = loader.format("classify_ticket", ticket_text="Login issue")
        """
        template = self.load(prompt_name)
        return template.format(**kwargs)