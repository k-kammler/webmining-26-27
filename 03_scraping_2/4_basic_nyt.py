from lxml import html
import requests


url = 'https://www.nytimes.com/search?dropmab=false&endDate=2024-11-01&lang=en&query=&sort=best&startDate=2024-10-01'

response = requests.get(url)
# Die NYT kann einfache Anfragen durch Bot-Schutz blockieren
# (z. B. Status 403). Manche Anfragen liefern jedoch HTML mit Ergebnissen.

if response.status_code == 200:
    html_content = response.text

    tree = html.fromstring(html_content)
    headlines = tree.cssselect('div[data-testid="search-bodega-result"] div[data-tpl="h"]')

    for headline in headlines:
        print(headline.text_content())

else:
    print(f"Fehler beim Abrufen der Seite: {response.status_code}")

