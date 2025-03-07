import os
from openai import OpenAI
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

class Chatbot:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY não encontrado. Verifique seu arquivo .env.")

        self.client = OpenAI(api_key=api_key)

    def ask(self, message):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message.content.strip()
