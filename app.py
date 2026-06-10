from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from datetime import datetime

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            'message': 'Hello from Docker!',
            'student': 'Lekan',
            'day': 'Day 17 of 30',
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        self.wfile.write(json.dumps(response).encode())
    
    def log_message(self, format, *args):
        pass

print("Server starting on port 8080...")
HTTPServer(('0.0.0.0', 8080), Handler).serve_forever()
