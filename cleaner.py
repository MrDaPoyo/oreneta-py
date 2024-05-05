import requests
import socket
from crawler import *

def checkURL(url, HTTPS=False): # check if website is up and running by Internet URL
    try:
        if HTTPS == True:
            x = requests.get("https://" + url)
        else:
            x = requests.get("http://" + url)
        print("Status code: " + str(x.status_code))

        if int(str(x.status_code)[:1]) == 2:
            print("OK")
            return True
        else:
            print("NOK")
            return False
    except Exception as exception:
        
        print(f"ERROR " + str(exception))
        return "ERR"

def read_url(location): # Reads urls.txt and transforms it into a clean list
    url = []
    try:
        with open(str(location), "r") as data:
            for info in data:
                as_list = info.split(",")
                url.append(as_list[0])
    except Exception as exception:
        return exception
    return url

def neocities(input):
    url = str(input + ".neocities.org")
    ip = socket.gethostbyname(url)
    return (f"{url}")

query_dns("wikipedia.org", "")


'''

# Test --> OK -> Domain exists and operative
checkURL("wikipedia.org")
# Test --> NOK -> Domain exists but not operative
checkURL("skibidi.org")
# Test --> ERR / Exception NameResolutionError -> Domain doesn't exist
checkURL("rosesareviolet.org")

# Test --> Returns a list
print(read_url("urls.txt"))
# Test --> Returns error "[Errno 2] No such file or directory: 'url.txt'"
print(read_url("url.txt"))

# Test
print(neocities("dapoyo"))

'''