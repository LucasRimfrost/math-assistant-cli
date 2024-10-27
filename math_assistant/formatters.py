"""Formatting utilities for Math Assistant responses."""

from typing import Union, Dict, List, Any, Optional, ClassVar
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.theme import Theme
import re
from datetime import datetime

ResponseType = Union[str, Dict[str, Any], List[Any]]  # Type alias for responses


class ResponseFormatter:
    """Handles formatting of responses from the Math Assistant."""

    # Class variables with explicit types
    BOLD: ClassVar[str] = "\033[1m"
    RESET: ClassVar[str] = "\033[0m"

    def __init__(self) -> None:
        """Initialize formatter with custom theme."""
        self.theme: Theme = Theme(
            {
                "info": "cyan",
                "warning": "yellow",
                "error": "red",
                "success": "green",
                "header": "blue bold",
            }
        )
        self.console: Console = Console(theme=self.theme)

    @staticmethod
    def clean_text(response: ResponseType) -> str:
        """Extract and clean text from response."""
        if isinstance(response, str) and "TextBlock" in response:
            match: Optional[re.Match] = re.search(r'text="(.*?)"', response, re.DOTALL)
            text: str = match.group(1) if match else response
        else:
            text = str(response)

        # Clean up the text
        text = text.replace("\\n", "\n")
        text = re.sub(r"\n\s+", "\n", text)  # Remove excess whitespace
        return text.strip()

    @classmethod
    def pretty_print(cls, response: ResponseType, show_sections: bool = True) -> None:
        """Format and print response with sections and formatting."""
        text: str = cls.clean_text(response)
        sections: List[str] = text.split("\n\n")

        for section in sections:
            if not section.strip():
                continue

            # Handle headers (ends with colon)
            if section.strip().endswith(":"):
                if show_sections:
                    print("\n" + "-" * 50)
                print(cls.BOLD + section.strip() + cls.RESET)

            # Handle numbered lists/steps
            elif section.strip() and section.strip()[0].isdigit() and ". " in section:
                header: str = section.split("\n")[0]
                rest: List[str] = section.split("\n")[1:]
                print("\n" + cls.BOLD + header + cls.RESET)
                for line in rest:
                    if line.strip():
                        print(line)

            # Regular text
            else:
                print(section)

    @classmethod
    def rich_print(
        cls,
        response: ResponseType,
        title: str = "Math Assistant Response",
        style: str = "blue",
    ) -> None:
        """Print response using rich formatting with colors and boxes."""
        console: Console = Console()
        text: str = cls.clean_text(response)

        # Convert text to markdown
        md: Markdown = Markdown(text)

        # Create panel with proper styling
        panel: Panel = Panel(
            md, title=title, border_style=style, padding=(1, 2), title_align="left"
        )

        # Print with proper spacing
        console.print()
        console.print(panel)
        console.print()

    @classmethod
    def to_markdown(
        cls, response: ResponseType, include_frontmatter: bool = False
    ) -> str:
        """Convert response to markdown format for saving or further processing."""
        text: str = cls.clean_text(response)

        # Add frontmatter if requested
        if include_frontmatter:
            frontmatter: str = f"""---
title: Math Assistant Response
date: {datetime.now().strftime('%Y-%m-%d')}
---

"""
            text = frontmatter + text

        # Convert common patterns to markdown
        text = re.sub(
            r"^(\d+)\.\s", r"\n\1. ", text, flags=re.MULTILINE
        )  # Numbered lists
        text = re.sub(
            r"^([A-Za-z ]+):$", r"\n## \1", text, flags=re.MULTILINE
        )  # Headers

        return text.strip() + "\n"

    def print_error(self, message: str) -> None:
        """Print error message in red."""
        self.console.print(f"[error]Error: {message}[/error]")

    def print_success(self, message: str) -> None:
        """Print success message in green."""
        self.console.print(f"[success]{message}[/success]")

    def print_warning(self, message: str) -> None:
        """Print warning message in yellow."""
        self.console.print(f"[warning]Warning: {message}[/warning]")
