import os
import chatgpt
from colors import Colors
from dotenv import load_dotenv
from os.path import join, dirname
from utils import clear_line


def main():
    # Load OpenAI API key from .env file
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    api_key = os.environ.get("OPENAI_API_KEY")
    chatgpt.init(api_key)

    # Header and instructions
    print("Welcome to ChatGPT CLI! Type 'exit', 'quit' or 'bye' to quit.\n")

    while True:
        # Get user input
        prompt = input("You: ")
        if prompt.lower() in ["exit", "quit", "bye"]:
            break

        # Print response
        print("\nThinking...")
        response = chatgpt.chat(prompt)
        clear_line()
        print("\rChatGPT: " + Colors.CYAN + response + "\n" + Colors.RESET)


if __name__ == '__main__':
    main()
