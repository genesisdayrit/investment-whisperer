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

    # Extract and print the headlines along with their hyperlinks
    for headline in headlines:
        # Extract the hyperlink associated with the headline (if it exists)
        link_tag = headline.find('a')
        if link_tag:
            link = link_tag['href']
            # Print the headline and its hyperlink
            print("Headline:", headline.text.strip())
            print("Link:", link)
            print()  # Add a blank line for separation
        else:
            # Print a message indicating that the hyperlink was not found
            print("Headline:", headline.text.strip())
            print("Link: Not found")
            print()  # Add a blank line for separation
else:
    print("Failed to fetch Yahoo Finance news. Status code:", response.status_code)
