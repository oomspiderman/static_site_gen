
def markdown_to_blocks(markdown):
    parts = markdown.split("\n\n")
    cleaned = []

    for part in parts:
        stripped = part.strip()
        if stripped:  # Only add non-empty parts
            cleaned.append(stripped)

    # OR ... cleaned = [part.strip() for part in markdown.split("\n\n") if part.strip()]

    return cleaned
    