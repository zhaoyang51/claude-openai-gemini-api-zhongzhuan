"""FastAI API quickstart example using the official OpenAI Python SDK."""

import os
from openai import OpenAI


def main() -> None:
    api_key = os.environ.get("FASTAI_API_KEY")
    if not api_key:
        raise ValueError(
            "Please set the FASTAI_API_KEY environment variable before running this script."
        )

    base_url = os.environ.get("FASTAI_BASE_URL", "https://www.fastaitoken.com/v1")
    model = os.environ.get("FASTAI_MODEL", "gpt-6.1-sol")

    client = OpenAI(api_key=api_key, base_url=base_url)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello! Please briefly introduce yourself."},
        ],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
