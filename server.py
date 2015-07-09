import sys
import json
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

jsonFile = open("myWebsites.json", "rw");
data = json.load(jsonFile);

print data["links_1"][0]["url"];


HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000
server_address = ('127.0.0.1', port)

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()