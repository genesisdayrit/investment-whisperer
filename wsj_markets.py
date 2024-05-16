import requests
from bs4 import BeautifulSoup

def scrape_wsj_headlines():
    # URL of the page to scrape
    url = 'https://www.wsj.com/news/markets'

    # Send a request to the website
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find elements containing headlines - this selector might need to be updated based on the site's structure
        headlines = soup.find_all('h3', class_='WSJTheme--headline--unZqjb45')  # Example class, adjust as necessary

        # Print each headline text
        for headline in headlines:
            print(headline.text.strip())
    else:
        print("Failed to retrieve the page. Status code:", response.status_code)

scrape_wsj_headlines()
