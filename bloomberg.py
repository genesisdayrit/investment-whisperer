import requests

# URL of Bloomberg API endpoint for market news
bloomberg_api_url = "https://api.bloomberg.com/news/articles"

# Parameters for the API request (example parameters, adjust as needed)
params = {
    "category": "markets",
    "format": "json",
    "limit": 10  # Limit the number of articles to retrieve
}

# Add any required authentication headers (consult Bloomberg API documentation)
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}

# Send an HTTP GET request to the Bloomberg API endpoint
response = requests.get(bloomberg_api_url, params=params, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract and print the headlines
    articles = data.get("articles", [])
    for article in articles:
        print(article.get("headline"))
else:
    print("Failed to fetch Bloomberg market news. Status code:", response.status_code)
