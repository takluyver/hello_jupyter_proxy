"""A minimal example server to run with jupyter-server-proxy
"""
import argparse
import socket
import sys
from copy import copy
from http.server import BaseHTTPRequestHandler, HTTPServer

__version__ = '0.1'

# This is the entry point for jupyter-server-proxy . The packaging metadata
# tells it about this function. For details, see:
# https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
def setup_hello():
    return {
        'command': [sys.executable, '-m', 'hello_jupyter_proxy', '{port}'],
        'unix': True,
    }

# Define a web application to proxy.
# You would normally do this with a web framework like tornado or Flask, or run
# something else outside of Python.
# This example uses Python's low-level http.server, to minimise dependencies.
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(TEMPLATE.format(
            path=self.path, headers=self._headers_hide_cookie()
        ).encode('utf-8'))

    def _headers_hide_cookie(self):
        # Not sure if there's any security risk in showing the Cookie value,
        # but better safe than sorry. You can inspect cookie values in the
        # browser.
        res = copy(self.headers)
        if 'Cookie' in self.headers:
            del res['Cookie']
            res['Cookie'] = '(hidden)'
        return res


TEMPLATE = """\
<!DOCTYPE html>
<html>
<head>
<title>Hello Jupyter-server-proxy</title>
</head>
<body>
<h1>Hello Jupyter-server-proxy</h1>
<p>Request path is <code>{path}</code></p>
<p>Headers:</p>
<pre>{headers}</pre>
</body>
</html>
"""

class HTTPUnixServer(HTTPServer):
    address_family = socket.AF_UNIX

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('port')
    args = ap.parse_args()

    # 127.0.0.1 = localhost: only accept connections from the same machine
    if args.port.isdigit():
        httpd = HTTPServer(('127.0.0.1', int(args.port)), RequestHandler)
    else:
        httpd = HTTPUnixServer(args.port, RequestHandler)
    print("Launching example HTTP server")
    httpd.serve_forever()

if __name__ == '__main__':
    main()
