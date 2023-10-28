# EX01 Developing a Simple Webserver
## Date: 20.09.2023

## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```python
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
```

## OUTPUT:
![WEB_EX01](https://github.com/Shakthikumar22009242/simplewebserver/assets/120207509/e58d21dc-1502-4916-8f2c-c96319786bf2)



## RESULT:
The program for implementing simple webserver is executed successfully.
