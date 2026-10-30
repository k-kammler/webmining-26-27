from boilerpy3 import extractors

url = 'https://www.heise.de/news/Rundfunkreform-ARD-Radioprogramme-werden-von-70-auf-53-reduziert-9995463.html'
extractor = extractors.ArticleExtractor()
article = extractor.get_content_from_url(url)

print(article)