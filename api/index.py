# api/index.py
import json
from http.server import BaseHTTPRequestHandler
    
from flask import Flask, request, jsonify

# class handler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type','application/json')
#         self.end_headers()
#         self.wfile.write(json.dumps({"message": "Hello!"}).encode('utf-8'))
#         return


app = Flask(__name__)

# Dummy marks data for names
marks_data = {
    "X": 10,
    "Y": 20,
    "Z": 15,  # You can add more names and marks here
}

@app.route('/api', methods=['GET'])
def get_marks():
    # Get the list of 'name' parameters from the query string
    names = request.args.getlist('name')
    
    # Get the corresponding marks for the names
    marks = [marks_data.get(name, None) for name in names]  # None for names not found
    
    # Return the response in JSON format
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True)