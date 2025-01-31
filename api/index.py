# api/index.py
import json
from http.server import BaseHTTPRequestHandler
from urllib import parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS by adding the appropriate headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow all origins
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

        # Parse query parameters
        query = parse.urlparse(self.path).query
        params = dict(parse.parse_qsl(query))

        # Get name parameter
        name = params.get("name", "World")

        # Respond with JSON
        self.wfile.write(json.dumps({"message": f"Hello, {name}!"}).encode('utf-8'))

    def do_OPTIONS(self):
        """ Handle CORS Preflight Requests """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
