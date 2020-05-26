from newspaper import Article
url = url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
article = Article(url)
article.download()
article.html
article.parse()

print(article.authors)
article.publish_date
article.text
article.top_image
article.movies
article.nlp()
article.keywords
article.summary



