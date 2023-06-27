'''
Name: Nelda John
Program: Web Scraping

'''

#importing
import requests
from bs4 import BeautifulSoup


		#---extract the 5-letter words of wordle
#request for data scrape
l = requests.get('https://www.rockpapershotgun.com/wordle-past-answers')
#parse the content
l_soup = BeautifulSoup(l.content, 'html.parser')
#find the specific div of the content
s = l_soup.find('div', id = "app_wrapper")
#find the list
l_words = s.find('ul', class_ = "inline")
#pick the individual items
l_content = l_words.find_all('li')
#create plain list
wordlist1 = []
#remove tags and append to list
for line in l_content:
    wordlist1.append(line.text)




		#---extract the 6-letter word list
#request for data scrape
m = requests.get('https://www.thefreedictionary.com/6-letter-words.htm')
#parse the content
m_soup = BeautifulSoup(m.content, 'html.parser')
#find the specific div of the content
t = m_soup.find('div', id = "dCont")
#find the list
m_words = t.find('ul')
#pick the individual items
m_content = m_words.find_all('li')
#create plain list
wordlist2 = []
#remove tags and append to list
for line in m_content:
	temp_word = line.text 
	wordlist2.append(temp_word.upper()) #append capitalized words




		#---extract the 7-letter word list
#request for data scrape
n = requests.get("https://byjus.com/english/7-letter-words/")
#parse the content
n_soup = BeautifulSoup(n.content, 'html.parser')
#find the specific div of the content (in this case, an article)
v = n_soup.find('article', id = 'post-1791424')
#find the table body
n_words = v.find('tbody')
#trim the individual items
n_content = n_words.find_all('td')
#create plain list
wordlist3 = []
#remove tags and append to list
for line in n_content:
	temp_word = line.text
	if len(temp_word) > 0:
		wordlist3.append(temp_word.upper())


#combine all the three lists
game_list = wordlist1 + wordlist2 + wordlist3
#sort the list alphabetically
game_list.sort()

#pass the list to the next python program
def passlist():
	return game_list





