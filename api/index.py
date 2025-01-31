import json
from http.server import BaseHTTPRequestHandler

# class handler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type','application/json')
#         self.end_headers()
#         self.wfile.write(json.dumps({"message": "Hello!"}).encode('utf-8'))

#         # with open(join('data', 'file.txt'), 'r') as file:
#         #   for line in file:
#         #     self.wfile.write(line.encode())
#         # return
#         return
    
def handler(request):
    # Extract the 'name' parameters from the query string
    names = request.args.getlist('name')
    
    marks_data = [{"name":"Qz8Y5uug","marks":18},{"name":"lKZelheI","marks":43},{"name":"MxNg3ItL","marks":32},{"name":"qaeqno","marks":20},{"name":"CMKPj","marks":8},{"name":"N3Ddd0T3","marks":81},{"name":"H2wSm19VC","marks":4},{"name":"q4LJFVI5K","marks":80},{"name":"8","marks":93},{"name":"VHlVPSTZ","marks":91},{"name":"ATo0CG","marks":70},{"name":"hRHf","marks":46},{"name":"NUbNnm36F","marks":79},{"name":"SfQ9jJN","marks":48},{"name":"O9j","marks":41}]
    
    # Get the corresponding marks for the names
    marks = [marks_data.get(name, None) for name in names]  # None for names not found
    
    # Return the response as JSON
    return {
        'statusCode': 200,
        'body': json.dumps({"marks": marks}),
        'headers': {
            'Content-Type': 'application/json',
        }
    }