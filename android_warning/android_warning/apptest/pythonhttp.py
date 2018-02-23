import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

print Handler
httpd = SocketServer.TCPServer(("172.18.7.94", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
