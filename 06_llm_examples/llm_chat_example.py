# Python client for full KI-Chat functionality can be found at: https://github.com/k-kammler/openwebui-client

import os
import sys
import requests
from dotenv import load_dotenv

url = "https://ki-chat.uni-mainz.de/api/chat/completions"
model = "deepseek-v4.1-flash"  # Verfügbare Modell-IDs liefert llm_models_example.py

# API Key kann auf ki-chat.uni-mainz.de generiert werden
# und wird in der Datei .env abgelegt: KI_CHAT_API_KEY=...
load_dotenv()
api_key = os.getenv("KI_CHAT_API_KEY")
if not api_key:
    sys.exit("Kein API-Key gefunden. Bitte in der Datei .env eintragen: KI_CHAT_API_KEY=...")

headers = {
    'Authorization': f'Bearer {api_key}'
}

data = {
    "model": model,
    "messages": [
        {
            "role": "user", 
            "content": "What is the capital of France?"
        }
    ]
}

response = requests.post(url, json=data, headers=headers)
 
if response.status_code == 200:
    result = response.json()
    print(result["choices"][0]["message"]["content"])
else:
    print(f"Error: {response.text}")