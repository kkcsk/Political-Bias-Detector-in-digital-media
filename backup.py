import newspaper
from newspaper import Article
import filter
from colorama import init 
from termcolor import colored 
init() 

print(colored("1.build", 'blue'))
print(colored("2.text(content)", 'blue'))
print(colored("3.print author", 'blue'))
print(colored("4.publish date", 'blue'))
print(colored("5.top image", 'blue'))
print(colored("6.VideoClip", 'blue'))
print(colored("7.Final Data Obtained", 'blue'))
print(" ")

while True:
	print("--------------------------------------------------------------------------------")
	ch=int(input("Enter your choice:"))
	print("--------------------------------------------------------------------------------")
	if ch==1:
		url = filter.url
		article = Article(url)
		article.download()
		article.html
		article.parse()
		list2 = [article.authors,article.publish_date]
		print(filter.url)
		print("Successful... ")
	if ch==2:
		print(" ")
		print("Text : ",article.text)
	elif ch==3:
		print(" ")
		print("Author : ",article.authors)
	elif ch==4:
		print(" ")
		print("Publish Date : ",article.publish_date)
	elif ch==5:
		print(" ")
		print("Top Image : ",article.top_image)
	elif ch==6:
		print(" ")
		print("Video Clip : ",article.movies)
	elif ch==7:
		print("-: The Final Data Obtained From Dataset and Web :-")
		print("--------------------------------------------------------------------------------")
		article.nlp()
		print("Keywords After Scraping : ",article.keywords)
		print(" ")
		print("Key Facts from dataset : ",filter.list1)
		print(" ")
		print("Summary : ",[article.summary])






