"""Coder for generating SwiftUI code from templates."""

from .ask_coder import AskCoder
from .generate_prompts import GeneratePrompts


class GenerateCoder(AskCoder):
    """Generate SwiftUI views from templates."""

    edit_format = "ask"  # Use ask format since we're not editing files
    gpt_prompts = GeneratePrompts()
