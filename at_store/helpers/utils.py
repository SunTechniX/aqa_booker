import re

def load_data(mutable_data: dict,
              tokens: str | list[str] | tuple[str],
              instance: str | list[str] | tuple[str]) -> None:
    if isinstance(tokens, str):
        mutable_data["csrftoken"] = tokens
        mutable_data["csrfinstance"] = instance
    else:
        mutable_data["csrftoken"] = tokens[0]
        mutable_data["csrfinstance"] = instance[0]


def extract_visible_errors(html: str) -> list[str]:
    """ Извлекает видимые сообщения об ошибках из HTML """
    errors = []
    # Удаляем скрипты, стили, комментарии
    clean = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)
    clean = re.sub(r'<script[^>]*>.*?</script>', '', clean,
                   flags=re.DOTALL | re.IGNORECASE)
    clean = re.sub(r'<style[^>]*>.*?</style>', '', clean,
                   flags=re.DOTALL | re.IGNORECASE)

    patterns = [
        r'<div[^>]*class="[^"]*alert[^"]*error[^"]*"[^>]*>(?:<button[^>]*></button>)?\s*([^<]+)</div>',
        r'<div[^>]*class="[^"]*error[^"]*"[^>]*>([^<]+)</div>',
        r'<span[^>]*class="[^"]*error[^"]*"[^>]*>([^<]+)</span>',
        r'(?:^|[\s>])(Error|Warning|Notice):\s*([^<\.\n]+)',
    ]
    for pattern in patterns:
        matches = re.findall(pattern, clean, flags=re.IGNORECASE)
        for match in matches:
            text = match[-1].strip() if isinstance(match,
                                                   tuple) else match.strip()
            if text and len(
                    text) < 150 and '<' not in text and not text.startswith(
                    ('function', 'var', 'if', '$')):
                errors.append(text)
    return list(dict.fromkeys(errors))
