import requests

import requests
import dns.resolver # NOTE: dnspython package
import tldextract
# Poyo; -Whatchu doing? Oooooooh cool!
# Security; - this is for sending requests using the Ucanet DNS server
class CustomAdapter(requests.adapters.HTTPAdapter):
    def __init__(self, nameservers):
        self.nameservers = nameservers
        super().__init__()

    def resolve(self, host, nameservers, record_type):
        dns_resolver = dns.resolver.Resolver()
        dns_resolver.nameservers = nameservers
        answers = dns_resolver.query(host, record_type)
        for rdata in answers:
            return str(rdata)

    def get_connection(self, url, proxies=None):
        ext = tldextract.extract(url)
        fqdn = ".".join([ ext.subdomain, ext.domain, ext.suffix ])

        print("FQDN: {}".format(fqdn))
        a_record = self.resolve(fqdn, nameservers, 'A')
        print("A record: {}".format(a_record))

        resolved_url = url.replace(fqdn, a_record) # NOTE: Replace first occurrence only
        print("Resolved URL: {}".format(resolved_url))

        return super().get_connection(resolved_url, proxies=proxies)


url = 'http://fuck.asia' # Test for a ucanet-only domain


nameservers = [ 
        '135.148.41.26'
]

session = requests.Session()
session.mount(url, CustomAdapter(nameservers))
response = session.get(url)
print(response)