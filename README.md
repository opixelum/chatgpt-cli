# ChatGPT CLI

ChatGPT but in your terminal.

## Getting Started

### Prerequisites

**Remember that you need credits for OpenAI API in order to use this script.**
Check your
[OpenAI API billing information](https://platform.openai.com/account/billing).

1. Clone this repo

   *Using SSH:*

   ```bash
   git clone git@github.com:opixelum/chatgpt-cli.git
   ```

   *Using HTTPS:*

   ```bash
   git clone https://github.com/opixelum/chatgpt-cli.git
   ```

2. Install `dotenv` & `openai` package:

   *Example using `pip`:*

   ```bash
   pip install dotenv openai
   ```

3. Copy `.env.example` into `.env`:

    ```bash
    cp .env.example .env
    ```

4. Fill `OPENAI_API_KEY` in `.env` with your OpenAI API key.

   ```text
    OPENAI_API_KEY=sk-...
    ```

### Usage

Run it!

 ```bash
 python main.py
 ```
