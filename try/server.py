from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import sqlite3
import os

# Connect to SQLite database (create if it doesn't exist)
con = sqlite3.connect('codes.db')
cur = con.cursor()

# Create table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS CodeSubmissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        code TEXT
    )
""")
con.commit()

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, content, status=200, content_type="text/html"):
        self.send_response(status)
        self.send_header("Content-type", content_type)
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))

    def do_GET(self):
        print("check")
        if self.path == "/":
            # Serve the index.html file
            with open("index.html", "r") as f:
                content = f.read()
                self._send_response(content)
        else:
            # Serve 404 for any other path
            self._send_response("<h1>404 Not Found</h1>", status=404)

    def do_POST(self):
        if self.path == "/submit":
            print("here")
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length).decode("utf-8")
            
            # Parse form data
            data = urllib.parse.parse_qs(post_data)
            username = data.get("username", [""])[0]
            code = data.get("code", [""])[0]
            print("here")
            # Insert data into SQLite database
            cur.execute("INSERT INTO CodeSubmissions (username, code) VALUES (?, ?)", (username, code))
            with open("test.py","w") as test:
                    print(code)
                    code=code
                    print("ere")
                    test.write(code)  

                    
            con.commit()

            # Respond with a success message
            response = f"<h1>Code submitted successfully by {username}!</h1>"
            self._send_response(response)
        else:
            self._send_response("<h1>404 Not Found</h1>", status=404)

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on http://127.0.0.1:{port}/")
    httpd.serve_forever()

if __name__ == "__main__":
    
    run()
