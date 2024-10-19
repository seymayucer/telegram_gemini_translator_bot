import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)
from gemini_translator import GeminiTranslator  # Import the GeminiTranslator class
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Now you can access the API keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# Initialize the GeminiTranslator

translator = GeminiTranslator(api_key=GEMINI_API_KEY)

# Language options
languages = {"English": "en", "Turkish": "tr", "Arabic": "ar"}


# Helper function to translate text based on AI-detected language
def auto_translate(update: Update, context: CallbackContext):
    text = update.message.text
    if not text:
        update.message.reply_text("Please provide text to translate.")
        return

    try:
        # Detect the language using Gemini itself
        detected_language = translator.detect_language(text)
    except Exception as e:
        update.message.reply_text(f"Error detecting language: {str(e)}")
        return

    # Prepare translations to other languages based on detected language
    translations = []
    if detected_language == "tr":
        # Translate Turkish to English and Arabic
        translations.append(translator.translate(text, "English"))
        translations.append(translator.translate(text, "Arabic"))
    elif detected_language == "en":
        # Translate English to Turkish and Arabic
        translations.append(translator.translate(text, "Turkish"))
        translations.append(translator.translate(text, "Arabic"))
    elif detected_language == "ar":
        # Translate Arabic to English and Turkish
        translations.append(translator.translate(text, "English"))
        translations.append(translator.translate(text, "Turkish"))
    else:
        # update.message.reply_text(
        #     "Sorry, I can only translate between English, Turkish, and Arabic."
        # )
        return

    # Respond with the parsed translations
    language_map = {
        "tr": ("English", "Arabic"),
        "en": ("Turkish", "Arabic"),
        "ar": ("English", "Turkish"),
    }

    target_languages = language_map.get(detected_language, None)
    if target_languages:
        response = f"{target_languages[0][0:2]}: {translations[0]}\n{target_languages[1][0:2]}: {translations[1]}"
        update.message.reply_text(response)
    else:
        update.message.reply_text(
            "Language not supported. Please use Turkish, English, or Arabic."
        )


# Command for help information
def help_command(update: Update, context: CallbackContext):
    help_text = (
        "Translator Bot\n\n"
        "This bot automatically detects and translates between Turkish, English, and Arabic using Google Gemini AI.\n"
        "Simply send a message in one of these languages, and the bot will translate it into the other two languages.\n\n"
        "Commands:\n"
    )
    update.message.reply_text(help_text)


# Command for settings (currently only shows language options)
def settings_command(update: Update, context: CallbackContext):
    language_keyboard = [["English", "Turkish", "Arabic"]]
    reply_markup = ReplyKeyboardMarkup(language_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        "The bot automatically translates between Turkish, English, and Arabic. You can select a language to see the settings.",
        reply_markup=reply_markup,
    )


# Main function to set up the bot
def main():
    # Set up the Updater and Dispatcher
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add handlers for commands
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("settings", settings_command))

    # Add a handler for messages (automatic translation)
    dispatcher.add_handler(
        MessageHandler(Filters.text & ~Filters.command, auto_translate)
    )

    # Start the bot
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
