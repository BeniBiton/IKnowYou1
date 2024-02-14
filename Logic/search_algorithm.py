'''
from bs4 import BeautifulSoup
import requests


html_text = requests.get("https://www.google.com/search?q=hi")

if html_text.status_code == 200:
    soup = BeautifulSoup(html_text.text, 'lxml')
    search_results = soup.find_all('span', dir='ltr')
    for result in search_results:
        print(result.text)
'''


import re
from bs4 import BeautifulSoup
import requests
from User import User
from collections import Counter

#adi evran
#leo messi

name = ""
html_text = requests.get(f"https://www.google.com/search?q=\"{name}\" site:instagram.com")
# Use the above line to perform a Google search with the name and site filter

# Check if the request was successful (status code 200)
if html_text.status_code == 200:
    soup = BeautifulSoup(html_text.text, 'lxml')
    search_results = soup.find_all('span', dir='ltr')

    print(len(search_results))

    for result in search_results:
        print(result.text)
else:
    print(f"Failed to retrieve the webpage. Status code: {html_text.status_code}")

users = []
location_count = 0

# Sample text
for result in search_results:
    text = result.text.replace("(", " ").replace(")", " ")
    pattern = r'\S*@\S+'

    # Use re.findall to find all words with '@'
    words_with_at_symbol = re.findall(pattern, text)

    if(len(words_with_at_symbol) != 0):

        in_users = False
        times_counter = 1
        for user in users:
            if(words_with_at_symbol == user.name):
                in_users = True
                user.amount_of_time = user.amount_of_time + times_counter
                times_counter += 1

        if(not in_users):
            user = User(words_with_at_symbol, location_count, times_counter)
            users.append(user)
            location_count += 1


    # Print the result
    for word in words_with_at_symbol:
        print(word)

for user in users:
    print("name: " + str(user.name[0]) + ". location: " + str(user.location) + ". amount: " + str(user.amount_of_time) + ". score: " + str(user.score()))