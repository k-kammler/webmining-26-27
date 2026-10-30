# Python client for full KI-Chat functionality can be found at: https://github.com/k-kammler/openwebui-client

import os
import sys
import requests
from dotenv import load_dotenv

# API Key kann auf ki-chat.uni-mainz.de generiert werden
# und wird in der Datei .env abgelegt: KI_CHAT_API_KEY=...
load_dotenv()
api_key = os.getenv("KI_CHAT_API_KEY")
if not api_key:
    sys.exit("Kein API-Key gefunden. Bitte in der Datei .env eintragen: KI_CHAT_API_KEY=...")

response = requests.get(
    "https://ki-chat.uni-mainz.de/api/models",
    headers={"Authorization": f"Bearer {api_key}"}
)

if response.status_code == 200:
    models = response.json()["data"]
    for model in models:
        print(model["id"])
else:
    print(f"Error: {response.text}")