import openai
import os
from os.path import join, dirname
from dotenv import load_dotenv


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


def main():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    openai.api_key = os.environ.get("OPENAI_API_KEY")

    print("Welcome to ChatGPT CLI! Type 'exit', 'quit' or 'bye' to quit.\n")

    while True:
        prompt = input("You: ")

        if prompt.lower() in ["exit", "quit", "bye"]:
            break


if __name__ == '__main__':
    main()
