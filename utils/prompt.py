"""
utils.py - Prompt initialization functions.
"""

import os
from pathlib import Path

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