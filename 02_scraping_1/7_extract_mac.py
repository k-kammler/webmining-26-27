import ssl
import urllib.request
import certifi
from boilerpy3 import extractors

url = 'https://www.heise.de/news/Rundfunkreform-ARD-Radioprogramme-werden-von-70-auf-53-reduziert-9995463.html'

# Mac: Python findet die Zertifikate des Systems nicht (CERTIFICATE_VERIFY_FAILED).
# Deshalb die Zertifikate aus dem Paket certifi verwenden (wird mit requests installiert).
ssl_context = ssl.create_default_context(cafile=certifi.where())

with urllib.request.urlopen(url, context=ssl_context) as response:
    html_content = response.read().decode('utf-8')

extractor = extractors.ArticleExtractor()
# Hinweis: ArticleExtractor behält nur den größten zusammenhängenden Textblock.
# Bei heise unterbricht der Kasten "Lesen Sie auch" den Artikel, daher fehlt hier
# der Schluss - Heuristiken sind nicht perfekt!
article = extractor.get_content(html_content)

print(article)