import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin



# URL of the webpage to scrape
url = 'https://www.w3schools.com/python/pandas/default.asp'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the title of the page
title = soup.title.string

web_link = url
# Extract the meta description of the page
meta_description = soup.find('meta', attrs={'name': 'Keywords'})

if meta_description is not None:
    meta_description = meta_description['content']
else:
    meta_description = None

print("Title:", title)
print("Description:", meta_description)
print("Url:", web_link)

print("Array of Links on the Page:")


links_array = [link.get('href') for link in soup.find_all('a') if link.get('href') is not None]

# Filter out None values and convert relative links to complete links
links_array = [urljoin(url, link) for link in links_array if link is not None]

# Print out the array of links
print(links_array)
print(len(links_array))

paragraphs = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

# Extract text content from paragraphs
page_text = ''
for element in paragraphs:
    page_text += element.get_text(separator=' ', strip=True) + '\n'

print(page_text)

print('0-100 print it att the monk of the main channel of the page')
print('the man is at the school. the name is to json of the man. in the beginning for the man. ')
print('the man is at the openai is at the base.')
