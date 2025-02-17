from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow requests from any domain
        self.send_header('Access-Control-Allow-Methods', 'GET')  # Allow only GET requests
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')  # Allow necessary headers
        self.end_headers()
        # Parse query parameters
        query_params = parse_qs(urlparse(self.path).query)

        # Extract names from the query parameters
        names = query_params.get("name", [])
        print(names)
        # Prepare response
        

        with open("./public/q-vercel-python.json", "r", encoding="utf-8") as file:
            marks_data = json.load(file)  # data is now a dictionary

        # Print the dictionary
        print(marks_data)
        result = []
        for name in names:
            # Find the entry where the name matches
            matching_entry = next((item for item in marks_data if item["name"] == name), None)
            if matching_entry:
                result.append(matching_entry["marks"])
            else:
                result.append(None)  # If name is not found, append None
    

        # Send HTTP response
        #self.send_response(200)
        #self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'marks':result}).encode('utf-8'))


    
# def handler(request):
#     # Extract the 'name' parameters from the query string
#     names = request.args.getlist('name')
    
#     marks_data = [{"name":"Qz8Y5uug","marks":18},{"name":"lKZelheI","marks":43},{"name":"MxNg3ItL","marks":32},{"name":"qaeqno","marks":20},{"name":"CMKPj","marks":8},{"name":"N3Ddd0T3","marks":81},{"name":"H2wSm19VC","marks":4},{"name":"q4LJFVI5K","marks":80},{"name":"8","marks":93},{"name":"VHlVPSTZ","marks":91},{"name":"ATo0CG","marks":70},{"name":"hRHf","marks":46},{"name":"NUbNnm36F","marks":79},{"name":"SfQ9jJN","marks":48},{"name":"O9j","marks":41}]
    
# # Get the corresponding marks for the names
#     result = []
#     for name in names:
#         # Find the entry where the name matches
#         matching_entry = next((item for item in marks_data if item["name"] == name), None)
#         if matching_entry:
#             result.append(matching_entry["marks"])
#         else:
#             result.append(None)  # If name is not found, append None
    
#     # Return the response as JSON
#     return {
#         'statusCode': 200,
#         'body': json.dumps({"marks": matching_entry}),
#         'headers': {
#             'Content-Type': 'application/json',
#         }
#     }