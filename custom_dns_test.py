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


nameservers = [ 
        '135.148.41.26'
]

print(query_dns("fuck.asia", "135.148.41.26")) # 135.148.41.26 = Ucanet's DNS IP

