#!/usr/bin/python
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class my_server(BaseHTTPRequestHandler):
    def do_GET(self):
        data = {"name": "John", "age": 30, "city": "New York"}
        json_data = json.dumps(data)

        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode("utf-8"))
        elif self.path.startswith("/data"):
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json_data.encode("utf-8"))
        elif self.path.startswith("/status"):
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write("OK".encode("utf-8"))
        else:
            self.send_error(404, "Not Found", "Endpoint Not Found")


port = HTTPServer(('', 8000), my_server)
port.serve_forever()
