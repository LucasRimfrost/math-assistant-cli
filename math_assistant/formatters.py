"""Formatting utilities for Math Assistant responses."""

from typing import Union, Dict, List
import re
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown


class ResponseFormatter:
    """Handles formatting of responses from the Math Assistant."""

    # ANSI escape codes for formatting
    BOLD = "\033[1m"
    RESET = "\033[0m"

    @staticmethod
    def clean_text(response: Union[str, Dict, List]) -> str:
        """Extract and clean text from response."""
        if isinstance(response, str) and "TextBlock" in response:
            match = re.search(r'text="(.*?)"', response, re.DOTALL)
            text = match.group(1) if match else response
        else:
            text = str(response)

        return text.replace("\\n", "\n")

    @classmethod
    def basic_print(cls, response: Union[str, Dict, List]) -> None:
        """Simple cleaned-up printing of response."""
        text = cls.clean_text(response)
        print(text)

    @classmethod
    def pretty_print(cls, response: Union[str, Dict, List]) -> None:
        """Format and print response with sections and formatting."""
        text = cls.clean_text(response)
        sections = text.split("\n\n")

        for section in sections:
            if section.strip():
                # Check if it's a header
                if section.strip().endswith(":"):
                    print("\n" + "-" * 50)
                    print(cls.BOLD + section.strip() + cls.RESET)
                else:
                    # Handle numbered lists
                    if section.startswith(("1.", "2.", "3.", "4.")):
                        header = section.split("\n")[0]
                        rest = section.split("\n")[1:]
                        print("\n" + cls.BOLD + header + cls.RESET)
                        for line in rest:
                            if line.strip():
                                print(line)
                    else:
                        print(section)

    @classmethod
    def rich_print(
        cls, response: Union[str, Dict, List], title: str = "Math Assistant Response"
    ) -> None:
        """Print response using rich formatting with colors and boxes."""
        console = Console()
        text = cls.clean_text(response)
        md = Markdown(text)
        console.print(Panel(md, title=title, border_style="blue"))

    @classmethod
    def to_markdown(cls, response: Union[str, Dict, List]) -> str:
        """Convert response to markdown format."""
        text = cls.clean_text(response)
        # Add any markdown formatting if needed
        return text
