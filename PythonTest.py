#from server import *

import urllib.request, urllib.error
from bs4 import BeautifulSoup

#import http.server
#import socketserver

#srv = Server()
#srv.accept()

#with socketserver.TCPServer(('127.0.0.1', 8000), http.server.SimpleHTTPRequestHandler) as httpd:
#    httpd.serve_forever()

url = "http://www.nikkei.com/"

html = urllib.request.urlopen(url)

soup = BeautifulSoup(html, "html.parser")

title_tag = soup.title

title = title_tag.string

print (title_tag)

print (title)
