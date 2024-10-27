"""Configuration settings for the Math Assistant."""

import os
from pathlib import Path


class Config:
    """Configuration settings."""

    # API settings
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

    # Image settings
    MAX_IMAGE_SIZE = 2048
    SUPPORTED_FORMATS = [".jpg", ".jpeg", ".png"]

    # Model settings
    DEFAULT_MODEL = "claude-3-5-sonnet-20241022"
    DEFAULT_MAX_TOKENS = 1500

    # File paths
    ROOT_DIR = Path(__file__).parent.parent
    CACHE_DIR = ROOT_DIR / ".cache"

    @classmethod
    def initialize(cls):
        """Initialize configuration and create necessary directories."""
        cls.CACHE_DIR.mkdir(parents=True, exist_ok=True)
