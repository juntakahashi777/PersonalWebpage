import os
import json
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

jsonFile = open("myWebsites.json", "rw");
data = json.load(jsonFile);

print data["links_1"][0]["url"];

class MyHandler(SimpleHTTPRequestHandler):
	def translate_path(self, path):
		root = os.getcwd()
		return root

if __name__ == '__main__':
	httpd = HTTPServer(('127.0.0.1', 8000), MyHandler)
	httpd.serve_forever()