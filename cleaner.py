import requests

def checkURL(url): # check if website is up and running by URL
    x = requests.get("http://" + url)
    print(x.status_code)

    if int(str(x.status_code)[:(int(len(str(x.status_code)))-1)]) == 2:
        return True
    else:
        return False

checkURL("wikipedia.com")