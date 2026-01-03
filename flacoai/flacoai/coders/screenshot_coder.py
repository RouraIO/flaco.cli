"""Coder for converting screenshots to SwiftUI code using vision models."""

from .ask_coder import AskCoder
from .screenshot_prompts import ScreenshotPrompts


class ScreenshotCoder(AskCoder):
    """Convert UI screenshots to SwiftUI code using vision models."""

    edit_format = "ask"  # Use ask format since we're not editing files
    gpt_prompts = ScreenshotPrompts()

    def supports_vision(self):
        """Check if the current model supports vision/image inputs.

        Returns:
            bool: True if model supports vision
        """
        # Check if model supports vision
        model_name = self.main_model.name.lower()

        # Known vision-capable models
        vision_models = [
            "gpt-4-vision",
            "gpt-4-turbo",
            "gpt-4o",
            "claude-3",
            "claude-opus",
            "claude-sonnet",
            "gemini",
            "llava",
            "qwen-vl",
        ]

        # Check if model name contains any vision model identifier
        for vision_model in vision_models:
            if vision_model in model_name:
                return True

        # Check model info for vision capability
        if hasattr(self.main_model, "info"):
            supports_vision = self.main_model.info.get("supports_vision", False)
            if supports_vision:
                return True

        return False
