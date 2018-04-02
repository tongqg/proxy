#!/usr/bin/env python
# author tongqg

from http.server import BaseHTTPRequestHandler, HTTPServer
import shutil, io

class EchoHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.outputtxt("hello world")

	def outputtxt(self, content):
		enc = "UTF-8"
		content = content.encode(enc)          
		f = io.BytesIO()
		f.write(content)
		f.seek(0)  
		self.send_response(200)  
		self.send_header("Content-type", "text/html; charset=%s" % enc)  
		self.send_header("Content-Length", str(len(content)))  
		self.end_headers()  
		shutil.copyfileobj(f,self.wfile)

def run():
    port = 8080
    print('starting server, port', port)

    # Server settings
    server_address = ('', port)
    httpd = HTTPServer(server_address, EchoHandler)
    print('running server...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()