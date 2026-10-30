from newspaper import Article

url = 'https://www.heise.de/news/Rundfunkreform-ARD-Radioprogramme-werden-von-70-auf-53-reduziert-9995463.html'

article = Article(url)
article.download()
article.parse()

print(article.text)