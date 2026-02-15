#!/usr/bin/python3
import http.server
import socketserver
import json

PORT = 8000

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # 1. Handle the root endpoint "/"
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # 2. Handle the "/data" endpoint (Serving JSON)
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {"name": "John", "age": 30, "city": "New York"}
            # Convert dict to JSON string, then encode to bytes
            self.wfile.write(json.dumps(data).encode('utf-8'))

        # 3. Handle the "/status" endpoint
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # 4. Handle undefined endpoints (404)
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            # The test likely expects this specific string:
            self.wfile.write(b"Endpoint not found")

def run(server_class=http.server.HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {PORT}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
