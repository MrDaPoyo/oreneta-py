import requests

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
        
        print(f"ERR " + str(exception))
        return "ERR"

def read_url(location):
    url = []
    with open(str(location), "r") as data:
        for info in data:
            as_list = info.split(f"/n")
            url.append(as_list[0])
    return url

print(read_url("urls.txt"))



# Test --> OK -> Domain exists and operative
checkURL("wikipedia.org")
# Test --> NOK -> Domain exists but not operative
checkURL("skibidi.org")
# Test --> ERR / Exception NameResolutionError -> Domain doesn't exist
checkURL("rosesareviolet.org")