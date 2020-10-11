"""
#import BautifulSoup library to pull data out of HTML and XML files
from bs4 import BeautifulSoup
import warnings
import pandas as pd
#import the python request library to query a website
import requests

#specify the url we want to scrape from
Link = "https://en.wikipedia.org/wiki/List_of_volcanoes_in_Indonesia"

#convert the web page to text
Link_text = requests.get(Link).text
#print(Link_text)

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

#to convert Link_text into a BeautifulSoup Object
soup = BeautifulSoup(Link_text, 'lxml')
#print(soup)

#make the indentation proper
#print(soup.prettify())

#Only the string not the tags
#print(soup.title.string)

#Fetch all the table tags
#all_table = soup.find_all('table')
#print(all_table)

#fetch all the table tags with class name="wikitable sortable"
our_table = soup.find('table', class_= "wikitable sortable")
#print(our_table)

#In the table that we will fetch find the <a> </a>tags
table_links = our_table.find_all('tr')
print(table_links)

#put the title into a list
vol = []
for links in table_links:
    vol.append(links.get('title'))
print(vol)

#Convert the list into a dataframe

df = pd.DataFrame(vol)
print(df)
"""

#################################################################################################
## -------------    Actual Code ----------------  ##

# import libraries
import requests
import pandas as pd
import csv
import urllib.request
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_volcanoes_in_Indonesia'
response = requests.get(url)
print(response.status_code)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.findAll('table', {"class": "sortable"})[0]
tr = table.findAll(['tr'])[0:50]
csvFile = open("Sumatra.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
try:
    for cell in tr:
        th = cell.find_all('th')
        th_data = [col.text.strip('\n') for col in th]
        td = cell.find_all('td')
        row = [i.text.replace('\n', '') for i in td]
        writer.writerow(th_data + row)

finally:
    csvFile.close()