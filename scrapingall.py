import newspaper
from newspaper import Article
print("1.build")
print("2.text(content)")
print("3.print author")
print("4.publish date")
print("5.top image")
print("6.Movies")
print("7.nlp")


while True:
	ch=int(input("Enter your choice"))
	if ch==1:
		papername = newspaper.build('http://www.sina.com.cn/', language='zh')
		for category in papername.category_urls():
			print(Catagory)
			article = papername.articles[0]
			article.download()
			article.html
			article.parse()
	if ch==2:
		print(" ")
		print("Text",article.text)
	elif ch==3:
		print(" ")
		print("Author",article.authors)
	elif ch==4:
		print(" ")
		print("Public Date",article.publish_date)
	elif ch==5:
		print(" ")
		print("Top Image",article.top_image)
	elif ch==6:
		print(" ")
		print("Movies",article.movies)
	elif ch==7:
		print(" ")
		article.nlp()
		print("Keywords",article.keywords)
		print(" ")
		print("Summary",article.summary)


#
#article.publish_date
#article.text
#article.top_image
#article.movies
#article.nlp()
#article.keywords
#article.summary



