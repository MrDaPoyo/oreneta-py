import requests

def checkURL(url, HTTPS=False): # check if website is up and running by URL
    if HTTPS == True:
        x = requests.get("https://" + url)
    else:
        x = requests.get("http://" + url)
    print(x.status_code)
    if int(str(x.status_code)[:1]) == 2:
        return True
    else:
        return False


# Test ->
print(checkURL("wikipedia.org"))