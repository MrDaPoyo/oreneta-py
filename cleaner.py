import requests

def checkURL(url, HTTPS=False): # check if website is up and running by URL
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


# Test --> OK
checkURL("wikipedia.org")