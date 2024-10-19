import os
import google.generativeai as genai
import json
import re


class GeminiLanguageDetector:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name="gemini-1.5-flash-002")

    def detect_language(self, text):
        # Prompt to ask Gemini to detect the language of the input text
        prompt = (
            f"Detect the language of the following text and provide the ISO language code:\n\n"
            f"Text: {text}\n\n"
            "Please return the language code in the following format:\n"
            "{\n"
            '  "language_code": "<detected_language_code>"\n'
            "}"
        )

        # Start the chat session
        chat_session = self.model.start_chat(history=[])

        try:
            response = chat_session.send_message(prompt)
            response_text = response.text

            # Extract the JSON-formatted language code from the response
            json_match = re.search(r"\{.*\}", response_text, re.DOTALL)
            if json_match:
                json_data = json.loads(json_match.group())
                return json_data.get(
                    "language_code", "und"
                )  # Return "und" if language_code not found
            else:
                return "und"  # "und" stands for undetermined language

        except Exception as e:
            return f"Error during language detection: {str(e)}"


class GeminiTranslator:
    def __init__(self, api_key):
        self.api_key = api_key
        genai.configure(api_key=self.api_key)

        # Initialize the Gemini language detector
        self.language_detector = GeminiLanguageDetector(api_key=self.api_key)

        # Create generation configuration for Gemini
        self.generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

        # Initialize the model for translation
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash-002",  # Ensure the model name is correct
            generation_config=self.generation_config,
        )

    def detect_language(self, text):
        # Use Gemini to detect the language of the text
        return self.language_detector.detect_language(text)

    def translate(self, text, target_language):
        # Start a new chat session
        chat_session = self.model.start_chat(history=[])

        # Create a translation prompt that requests JSON output
        prompt = (
            f"Translate this text to {target_language}: {text}\n\n"
            "Please provide the translation in the following JSON format:\n"
            "{\n"
            '  "translation": "<translated_text>"\n'
            "}"
        )

        try:
            # Send the translation request
            response = chat_session.send_message(prompt)
            response_text = response.text  # Get the full text of the response

            # Extract the JSON-formatted translation
            json_match = re.search(r"\{.*\}", response_text, re.DOTALL)

            if json_match:
                json_data = json.loads(json_match.group())
                return json_data.get("translation", "No translation found.")
            else:
                return "Unable to parse the response as JSON."

        except Exception as e:
            return f"Error during translation: {str(e)}"
