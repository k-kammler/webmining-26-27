import time
import random
import requests

for _ in range(10):
    response = requests.get('https://example.com')
    print(response.text[:100])
    
    time.sleep(random.uniform(5, 20))  
