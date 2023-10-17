import openai
import os
from os.path import join, dirname
from dotenv import load_dotenv


def main():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    print(os.getenv("OPENAI_API_KEY"))


if __name__ == '__main__':
    main()
