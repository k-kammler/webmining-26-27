import ssl
import urllib.request
from boilerpy3 import extractors

url = 'https://www.heise.de/news/Rundfunkreform-ARD-Radioprogramme-werden-von-70-auf-53-reduziert-9995463.html'

ssl_context = ssl._create_unverified_context()

with urllib.request.urlopen(url, context=ssl_context) as response:
    html_content = response.read().decode('utf-8')

extractor = extractors.ArticleExtractor()
article = extractor.get_content(html_content)

print(article)