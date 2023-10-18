import os
import chatgpt
from os.path import join, dirname
from dotenv import load_dotenv
from colors import Colors
from utils import clear_line


def main():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    api_key = os.environ.get("OPENAI_API_KEY")
    chatgpt.init(api_key)

    print("Welcome to ChatGPT CLI! Type 'exit', 'quit' or 'bye' to quit.\n")

    while True:
        prompt = input("You: ")

        if prompt.lower() in ["exit", "quit", "bye"]:
            break

        print("\nThinking...")
        response = chatgpt.chat(prompt)
        clear_line()
        print("\rChatGPT: " + Colors.CYAN + response + "\n" + Colors.RESET)


if __name__ == '__main__':
    main()
