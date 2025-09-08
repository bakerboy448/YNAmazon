import re

MARKDOWN_LINK_PATTERN = re.compile(r"\[([^\]]+)\]\([^\)]+\)")
MARKDOWN_BOLD_PATTERN = re.compile(r"\*\*([^*]+)\*\*")


def normalize_memo(memo: str) -> str:
    """Normalize a memo by joining any split lines that contain a URL."""
    lines = memo.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    result: list[str] = []
    current_line = ""
    in_url = False

    for line in lines:
        stripped = line.strip()
        if "amazon.com" in line:
            current_line += stripped
            in_url = True
        elif in_url and (stripped.endswith("-") or stripped.endswith(")")):
            # If we're in a URL and the line ends with a hyphen or closing parenthesis
            current_line += stripped
            if stripped.endswith(")"):
                in_url = False
                result.append(current_line)
                current_line = ""
        elif in_url:
            # If we're in a URL but the line doesn't end with a hyphen
            current_line += stripped
        else:
            if current_line:
                result.append(current_line)
                current_line = ""
            result.append(line)

    if current_line:
        result.append(current_line)

    return "\n".join(result)


def extract_order_url(memo: str) -> str | None:
    """Extract the Amazon order URL from a memo, handling both markdown and non-markdown formats."""
    # First normalize the memo to handle split lines
    normalized_memo = normalize_memo(memo)

    # First try to find a markdown URL
    markdown_url_match = re.search(
        r"\[Order\s*#[\w-]+\]\((https://www\.amazon\.com/gp/your-account/order-details\?orderID=[\w-]+)\)",
        normalized_memo,
    )
    if markdown_url_match:
        return markdown_url_match.group(1)

    # If no markdown URL found, look for a plain URL
    plain_url_match = re.search(
        r"https://www\.amazon\.com/gp/your-account/order-details\?orderID=[\w-]+", normalized_memo
    )
    if plain_url_match:
        return plain_url_match.group(0)

    return None


def remove_markdown_links(memo: str) -> str:
    """Remove markdown links from a memo, leaving just the link text."""
    return MARKDOWN_LINK_PATTERN.sub(r"\1", memo)


def remove_markdown_bold(markdown_memo: str) -> str:
    """Remove markdown bold formatting from a memo, leaving just the bold text."""
    return MARKDOWN_BOLD_PATTERN.sub(r"\1", markdown_memo)
