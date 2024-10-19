# 🧠 Google Gemini AI-Powered Translation Telegram Bot

This project is an ad-free **Telegram bot** that leverages **Google Gemini AI** to detect and translate text between **English**, **Turkish**, and **Arabic**. The bot automatically detects the input language using **Google Gemini** and translates the text into the other two languages. The bot uses **Python** and is configured to keep your API keys secure using **environment variables**.

## Features
- 🧠 **AI-powered language detection** using **Google Gemini**.
- 🌍 **Translations** between **English**, **Turkish**, and **Arabic**.
- 🔒 **Secure API key management** using `.env` files and environment variables.
- 🚀 Easily extendable for more languages or features.

---

## 📦 Project Structure

```bash
├── gemini_bot.py              # Main bot code
├── gemini_translator.py       # Gemini Translator class
├── .gitignore                 # Git ignore file for sensitive files
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```
---


## 🛠️ Prerequisites

- Python 3.8+
- Telegram Bot Token
- Google Gemini API Key


### Step-by-step Guide

1. **Clone the repository**:
   ```bash
   git clone https://github.com/seymayucer/telegram_gemini_translator_bot.git
   cd telegram_gemini_translator_bot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Create a `.env` file in the root of the project.
   - Add your `TELEGRAM_BOT_TOKEN` and `GEMINI_API_KEY` to the `.env` file.
   - Example `.env` file:
     ```
     TELEGRAM_BOT_TOKEN=your_telegram_bot_token
     GEMINI_API_KEY=your_gemini_api_key
     ```

4. **Run the bot**:
   In the terminal, run the following command to start the bot:
   
   ```bash
   python gemini_bot.py
   ```

## 🚀 Usage

Start the bot: Once the bot is running, you can interact with it through your Telegram bot by sending messages in English, Turkish, or Arabic. The bot will detect the language and automatically translate the message into the other two languages.



```bash
/help - Get help about how to use the bot.
```

### 📧 Support

If you need help or have any questions, feel free to open an issue or contact [me](mailto:seymayucer@gmail.com).


### 📖 Dependencies

- [python-telegram-bot](https://python-telegram-bot.readthedocs.io/en/stable/) - For building Telegram bots easily in Python.
- [Google Gemini API](https://ai.google.dev/gemini-api/docs) - For AI-powered language detection and translation. (see [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/))
- [python-dotenv](https://github.com/theskumar/python-dotenv) - For managing environment variables easily.
---