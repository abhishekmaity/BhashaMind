# backend-python/app/utils/prompt_templates.py

def get_zero_shot_prompt(label: str, lang: str = "bn") -> str:
    """
    Returns a natural language hypothesis template for zero-shot classification.
    Supports Bengali (bn) and English (en).

    Args:
        label (str): The candidate label/category.
        lang (str): Language code ("bn" or "en").

    Returns:
        str: Natural language hypothesis string.
    """
    if lang == "bn":
        return f"এই পাঠ্যটি {label} সম্পর্কে।"
    else:
        return f"This text is about {label}."
