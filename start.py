#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import glob

class TheHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
   
        message = ""
        for f in glob.glob('/repos/**/*.git', recursive=True):
            message += f
            message += '\n'

        for f in glob.glob('/repos/**/*.bin', recursive=True):
            message += f
            message += '\n'

        self.wfile.write(bytes(message, "utf8"))
        return
 
server_address = ('', 8888)
httpd = HTTPServer(server_address, TheHandler)
print('running server on port 8888...')
httpd.serve_forever()
