import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to scrape page title and metadata from a given URL
def scrape_page_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title of the page
    title = soup.title.string if soup.title else "No Title Found"

    # Prepare a list of possible meta tag names
    possible_meta_tags = ['description', 'Keywords', 'keywords']

    # Find and extract meta description (considering multiple tags)
    meta_description = None
    for tag_name in possible_meta_tags:
        meta_tag = soup.find('meta', attrs={'name': tag_name})
        if meta_tag:
            meta_description = meta_tag['content']
            break  # Exit the loop after finding a description

    # Handle case where no description is found
    meta_description = meta_description if meta_description else "No Meta Description Found"

    return title, meta_description

# URL of the webpage to scrape
url = 'https://www.britannica.com/'

# Send a GET request to the URL
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the title of the page
title = soup.title.string

web_link = url

# Extract the meta description of the page
meta_description = soup.find('meta', attrs={'name': 'description'})

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

# Extract and print information from the first link in links_array

    # Extract and print information from the first ten valid links in links_array
valid_links_array = [link for link in links_array if not link.startswith('javascript:')]
for index, link in enumerate(valid_links_array[:10], start=1):
    link_info = scrape_page_info(link)
    print(f"\nInformation from Link {index}:")
    print("Title:", link_info[0])
    print("Description:", link_info[1])
    print("URL:", link)

    # Extract text content from each link
    link_soup = BeautifulSoup(requests.get(link).content, 'html.parser')
    link_paragraphs = link_soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    link_page_text = ''
    for element in link_paragraphs:
        link_page_text += element.get_text(separator=' ', strip=True) + '\n'
    print("Text from Link:", link_page_text)