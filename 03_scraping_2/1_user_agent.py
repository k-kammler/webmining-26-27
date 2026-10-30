from fake_useragent import UserAgent
import requests

ua = UserAgent()

for _ in range(100):
    random_user_agent = ua.random
    print(random_user_agent)

#headers = {'User-Agent': random_user_agent}
#response = requests.get('https://example.com', headers=headers)

# ...