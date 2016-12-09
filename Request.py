import sys
import requests

class Request(object):
    authzToken = "123"
    url = "localhost"
    port = 80
    headers = None
    params = None

    def send(self, url, method, data, headers):
        #proxyUrls={'http': 'http://localhost:8080',	'https': 'http://localhost:8080'}
		proxyUrls={}
		if headers is None:
			headers={}
		req = requests.request(method, url, proxies=proxyUrls, data=data, headers=headers, verify=False)
		return req

#if __name__ == '__main__':
#     req = Request()
#     res = req.send("http://wikipedia.fr", 80, 'GET', None)
#     print "status code: " + str(res.status_code)


