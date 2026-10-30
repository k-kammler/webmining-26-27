from boilerpy3 import extractors

url = 'https://www.heise.de/news/Rundfunkreform-ARD-Radioprogramme-werden-von-70-auf-53-reduziert-9995463.html'
extractor = extractors.ArticleExtractor()
# Hinweis: ArticleExtractor behält nur den größten zusammenhängenden Textblock.
# Bei heise unterbricht der Kasten "Lesen Sie auch" den Artikel, daher fehlt hier
# der Schluss - Heuristiken sind nicht perfekt!
article = extractor.get_content_from_url(url)

print(article)