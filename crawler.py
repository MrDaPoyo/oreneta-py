"https://en.wikipedia.org/wiki/Dyslexia"
'''

TODO:
- Feed the crawler
- Store the data

'''

import requests
from bs4 import BeautifulSoup
import json
import requests
import dns.resolver # NOTE: Dnspython package

# Poyo; -Whatchu doing? Oooooooh cool!
# Security; - this is for sending requests using the Ucanet DNS server

def query_dns(domain, dns_server):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [dns_server]
    
    try:
        answers = resolver.resolve(domain) # Queries the domain to the dns server
        for rdata in answers:
            print(rdata)
    except dns.exception.DNSException as e:
        print("Error:", e)


nameservers = '135.148.41.26'


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



urls = json.load(open("urls.json"))
# print(urls)

ips = []
web_data = {}

# urls.json, has urls as the key name with the big list, so urls.urls will give big array
for item in urls["urls"]: #
    try:
        # print(item)
        ip = query_dns(item, "135.148.41.26")
        web_data[item] = fetch_body_text(f"http://{item}")
        # print(fetch_body_text(f"http://{item}"))
    except Exception:
        pass
    # ips.append(ip)



# save web_data to file here
#i dunno how to code that
# ahhhh

# print(ips)
# print("------")
# query_dns("google.com", nameservers)