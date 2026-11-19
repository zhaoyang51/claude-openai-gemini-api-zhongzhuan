"""AIHub API quickstart example using the official OpenAI Python SDK."""

import os
from openai import OpenAI


def main() -> None:
    api_key = os.environ.get("AIHUB_API_KEY")
    base_url = os.environ.get("AIHUB_BASE_URL")
    model = os.environ.get("AIHUB_MODEL", "gpt-4o-mini")

    if not api_key or not base_url:
        raise ValueError(
            "Please set AIHUB_API_KEY and AIHUB_BASE_URL environment variables "
            "from your AIHub console before running this script."
        )

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
