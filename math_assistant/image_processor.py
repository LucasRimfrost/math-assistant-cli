"""Image processing utilities for Math Assistant."""

from PIL import Image
import io
import base64
from pathlib import Path
from typing import Union, Tuple
from .exceptions import ImageProcessingError
from .config import Config


class ImageProcessor:
    """Handles image processing operations."""

    @staticmethod
    def validate_image(image_path: Union[str, Path]) -> Path:
        """Validate image file exists and has supported format."""
        path = Path(image_path)
        if not path.exists():
            raise ImageProcessingError(f"Image file not found: {path}")
        if path.suffix.lower() not in Config.SUPPORTED_FORMATS:
            raise ImageProcessingError(f"Unsupported image format: {path.suffix}")
        return path

    @staticmethod
    def process_image(image_path: Union[str, Path]) -> Tuple[str, Tuple[int, int]]:
        """Process and encode image for API submission."""
        try:
            path = ImageProcessor.validate_image(image_path)

            with Image.open(path) as img:
                # Convert to RGB if necessary
                if img.mode != "RGB":
                    img = img.convert("RGB")

                # Resize if needed
                original_size = img.size
                if max(original_size) > Config.MAX_IMAGE_SIZE:
                    ratio = Config.MAX_IMAGE_SIZE / max(original_size)
                    new_size = tuple(int(dim * ratio) for dim in original_size)
                    img = img.resize(new_size, Image.Resampling.LANCZOS)

                # Convert to base64
                buffer = io.BytesIO()
                img.save(buffer, format="JPEG")
                encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")

                return encoded, img.size

        except Exception as e:
            raise ImageProcessingError(f"Error processing image: {str(e)}")
