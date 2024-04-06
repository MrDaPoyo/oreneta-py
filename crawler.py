"https://en.wikipedia.org/wiki/Dyslexia"

import requests
from bs4 import BeautifulSoup

# Function to fetch the body text from a given URL
def fetch_body_text(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find the text content within the <body> tag
            body_text = soup.body.get_text()
            
            return body_text
        else:
            print(f"Failed to fetch {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred while fetching {url}: {e}")
        return None

# List of URLs to fetch
urls = [
    "https://en.wikipedia.org/wiki/Dyslexia",
    # Add more URLs as needed
]

# Iterate through the list of URLs
for url in urls:
    print(f"Fetching {url}...")
    
    # Fetch body text from the URL
    body_text = fetch_body_text(url)
    
    # Print the body text if available
    if body_text:
        print("Body Text:")
        print(body_text)
        print("-----------------------------")