# Python program to scrape website data using requests and BeautifulSoup

import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://baidu.com'

# Send an HTTP request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find elements by tag name
for paragraph in soup.find_all('p'):
    print(paragraph.text)

# Find elements by class name
for item in soup.find_all(class_='search_box'):
    print(item.text)
