import requests
from bs4 import BeautifulSoup

# URL of Yahoo Finance's news section
yahoo_finance_url = "https://finance.yahoo.com/news/"

# Send an HTTP GET request to the URL
response = requests.get(yahoo_finance_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the headlines within the specified HTML elements
    headlines = soup.find_all('h3')

    # Print the headlines
    for headline in headlines:
        print(headline.text.strip())
else:
    print("Failed to fetch Yahoo Finance news. Status code:", response.status_code)
