import openai
import os
from os.path import join, dirname
from dotenv import load_dotenv
from colors import Colors
from utils import clear_line


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

        print("\nThinking...")
        response = chat_with_gpt(prompt)
        clear_line()
        print("\rChatGPT: " + Colors.CYAN + response + "\n" + Colors.RESET)


if __name__ == '__main__':
    main()
