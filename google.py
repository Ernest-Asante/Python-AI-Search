import requests
from bs4 import BeautifulSoup





def scrape_page_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title of the page
    title = soup.title.string if soup.title else "No Title Found"

    # Prepare a list of possible meta tag names
    possible_meta_tags = ['description', 'Keywords', 'keywords' ,'metadata']

    # Find and extract meta description (considering multiple tags)
    meta_description = None
    for tag_name in possible_meta_tags:
        meta_tag = soup.find('meta', attrs={'name': tag_name})
        if meta_tag:
            meta_description = meta_tag['content']
            break  # Exit the loop after finding a description

    # Handle case where no description is found
    meta_description = meta_description if meta_description else "No Meta Description Found"

   


    return  title,meta_description
      




API_KEY = "AIzaSyBozBKoer2PI00pheCSXU2V8sNOgdT5urM"
SEARCH_ENGINE_ID = "d27ac8cafeab74577"

search_guery = "What is computer science"

url = "https://www.googleapis.com/customsearch/v1"

params = {
    'q' : search_guery,
    'key' : API_KEY,
    'cx' : SEARCH_ENGINE_ID,
    'num' : 3
   # 'searchType' : 'image'
}

response = requests.get(url, params = params)
results = response.json()

links_array = []

for item in results['items']:
     link = item['link']
     print(link)
     links_array.append(link)
    # Join links with commas and store in a new variable
all_links = ", ".join(links_array)
print(all_links)
print(links_array)

docs = ""

for index, link in enumerate(links_array[:3], start=1):
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










