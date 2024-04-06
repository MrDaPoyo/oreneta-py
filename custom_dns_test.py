import requests


class HostHeaderSSLAdapter(requests.adapters.HTTPAdapter):
    def resolve(self, hostname):
        # a dummy DNS resolver
        import random
        ips = [
            '104.16.89.20',  # CloudFlare
        ]
        resolutions = {
            'cdn.jsdelivr.net': random.choice(ips),
        }
        return resolutions.get(hostname)

    def send(self, request, **kwargs):
        from urllib.parse import urlparse

        connection_pool_kwargs = self.poolmanager.connection_pool_kw

        result = urlparse(request.url)
        resolved_ip = self.resolve(result.hostname)

        if result.scheme == 'https' and resolved_ip:
            request.url = request.url.replace(
                'https://' + result.hostname,
                'https://' + resolved_ip,
            )
            connection_pool_kwargs['server_hostname'] = result.hostname  # SNI
            connection_pool_kwargs['assert_hostname'] = result.hostname

            # overwrite the host header
            request.headers['Host'] = result.hostname
        else:
            # theses headers from a previous request may have been left
            connection_pool_kwargs.pop('server_hostname', None)
            connection_pool_kwargs.pop('assert_hostname', None)

        return super(HostHeaderSSLAdapter, self).send(request, **kwargs)


url = 'https://cdn.jsdelivr.net/npm/bootstrap/LICENSE'

session = requests.Session()
session.mount('https://', HostHeaderSSLAdapter())

r = session.get(url)
print(r.headers)

r = session.get(url)
print(r.headers)