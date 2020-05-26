import newspaper
from newspaper import Article
import filter
from colorama import init 
from termcolor import colored 
init() 

print(colored("1.build", 'blue'))
print(colored("2.text(content)", 'blue'))
print(colored("3.Final Data Obtained", 'blue'))
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
		print("Successful...")
	if ch==2:
		print(" ")
		print("Text : ",article.text)		
		
	elif ch==3:
		print("-: The Final Data Obtained From Dataset and Web :-")
		print("--------------------------------------------------------------------------------")
		article.nlp()
		print("Keywords After Scraping : ",article.keywords)
		print(" ")
		print("Key Facts from dataset : ",filter.list1)
		print(" ")
		print("Top Image : ",article.top_image)
		print(" ")
		print("Video Clip : ",article.movies)
		print(" ")	
		print("Summary : ",[article.summary])
		
		





