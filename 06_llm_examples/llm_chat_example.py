# Python client for full KI-Chat functionality can be found at: https://github.com/k-kammler/openwebui-client

import requests

url = "https://ki-chat.uni-mainz.de/api/chat/completions"

# API Key kann auf ki-chat.uni-mainz.de generiert werden
headers = {
    'Authorization': 'Bearer YOUR_API_KEY_HERE'
}

data = {
    "model": "GPT OSS 120B",
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