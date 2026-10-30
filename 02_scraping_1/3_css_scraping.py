from lxml import html
import requests

url = 'https://www.heise.de/news/Rundfunkreform-ARD-Radioprogramme-werden-von-70-auf-53-reduziert-9995463.html'

response = requests.get(url)

if response.status_code == 200:
    html_content = response.text

    tree = html.fromstring(html_content)
    links = tree.cssselect('a')

    hrefs = [link.get('href') for link in links if link.get('href') is not None]

    for href in hrefs:
        print(href)
else:
    print(f"Fehler beim Abrufen der Seite: {response.status_code}")

