from lxml import html
import requests
import re

url = 'https://www.heise.de/news/Rundfunkreform-ARD-Radioprogramme-werden-von-70-auf-53-reduziert-9995463.html'

response = requests.get(url)

if response.status_code == 200:
    html_content = response.text

    tree = html.fromstring(html_content)
    elements = tree.cssselect('div.article-content') 

    raw_text = elements[0].text_content()

    #print(raw_text)

    # Ersetzt mehrere aufeinanderfolgende Leerzeichen
    clean_text = re.sub(r'\s+', ' ', raw_text).strip()

    print(clean_text)
else:
    print(f"Fehler beim Abrufen der Seite: {response.status_code}")

