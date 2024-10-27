"""Utility functions for Math Assistant."""

import logging
from pathlib import Path
from typing import Optional


def setup_logging(log_file: Optional[Path] = None) -> None:
    """Set up logging configuration."""
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    if log_file:
        logging.basicConfig(
            level=logging.INFO,
            format=format,
            handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
        )
    else:
        logging.basicConfig(level=logging.INFO, format=format)
