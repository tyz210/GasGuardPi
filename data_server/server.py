import http.server
import socketserver
import time

from read_configuration import PORT_NUMBER

HOST_NAME = "localhost"


class MyServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p>This is a test.</p>", "utf-8"))
        self.wfile.write(bytes("<p>You accessed path: {}</p>".format(self.path), "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


with socketserver.TCPServer(("", PORT_NUMBER), MyServer) as httpd:
    print("{} Server Starts - {}:{}".format(time.asctime(), HOST_NAME, PORT_NUMBER))
    httpd.serve_forever()

httpd.server_close()
print("{} Server Stops - {}:{}".format(time.asctime(), HOST_NAME, PORT_NUMBER))
