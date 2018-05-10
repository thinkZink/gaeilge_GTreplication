from bs4 import BeautifulSoup
import urllib, urllib.request

#thanks, StackOverflow, for the solid table-scraping code.

#pull the HTML from the Indigenous Tweets website's Gaeilge page
response = urllib.request.urlopen('http://indigenoustweets.com/ga/')
#read the webpage, print out the content to verify
html = response.read()
print(html)

soup = BeautifulSoup(html) #will use lxml and warn of such if no parser specified otherwise

table = soup.find("table", attrs={"class":"tablesorter"})
headings = [th.get_text() for th in table.find("tr").find_all("th")]
datasets = []

for row in table.find_all("tr")[1:]:
	dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
	datasets.append(dataset)

for dataset in datasets:
	counter = 0 #we only want to print the twitter handle, field...1?
	for field in dataset:
		if (counter is 1):
			print("{1}".format(field[0], field[1]))
		counter += 1


