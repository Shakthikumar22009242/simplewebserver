from http.server import HTTPServer, BaseHTTPRequestHandler
content =""" 
<!DOCTYPE html>
<html>
<head>
<title>My webserver</title>
</head>
<body>
<h2 align="center">Upcoming Biggies </h2>
<hr>
<ol>
<h3>
<li>LEO</li>
<li>JAPAN</li>
<li>CAPTAIN MILLER</li>
<li>AYALAAN</li>
<li>RAGE</li>
</h3>
</ol>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()