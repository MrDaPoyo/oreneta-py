import requests
import ipaddress

def checkURL(url):
    x = requests.get("http://", url)
    print(x.status_code)

    if int(str(x.status_code)[:2]) == 2:
        return True
    else:
        return False

def checkIP(ip):
    try:
        ip_object = ipaddress.ip_address(ip)
        return True
    except:
        return False


