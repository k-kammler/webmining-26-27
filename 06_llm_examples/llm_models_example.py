# Python client for full KI-Chat functionality can be found at: https://github.com/k-kammler/openwebui-client

import requests

# API Key kann auf ki-chat.uni-mainz.de generiert werden
response = requests.get(
    "https://ki-chat.uni-mainz.de/api/models",
    headers={"Authorization": "Bearer YOUR_API_KEY_HERE"}
)

models = response.json()["data"]
for model in models:
    print(model["id"])