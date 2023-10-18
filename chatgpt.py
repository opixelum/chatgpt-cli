import openai
from colors import Colors


def init(api_key):
    openai.api_key = api_key


def chat(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
    except openai.error.RateLimitError:
        return Colors.RED + "Looks like you've hit the API rate limit, or "\
            "your account is out of credits. Check "\
            "https://platform.openai.com/account/billing and try again later."\
            + Colors.RESET

    return response.choices[0].message.content.strip()
