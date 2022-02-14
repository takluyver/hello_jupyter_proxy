"""A minimal example server to run with jupyter-server-proxy
"""
import argparse
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

__version__ = '0.1'

# This is the entry point for jupyter-server-proxy . The packaging metadata
# tells it about this function. For details, see:
# https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
def setup_hello():
    return {
        'command': [sys.executable, '-m', 'hello_jupyter_proxy', '{port}']
    }

# Define a web application to proxy.
# You would normally do this with a web framework like tornado or Flask, or run
# something else outside of Python.
# This example uses Python's low-level http.server, to minimise dependencies.
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(
            TEMPLATE.format(path=self.path, headers=self.headers).encode('utf-8')
        )


TEMPLATE = """\
<!DOCTYPE html>
<html>
<head>
<title>HTML 5 Boilerplate</title>
</head>
<body>
<h1>Hello Jupyter-server-proxy</h1>
<p>Request path is <code>{path}</code></p>
<p>Headers:</p>
<pre>{headers}</pre>
</body>
</html>
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('port', type=int)
    args = ap.parse_args()

    httpd = HTTPServer(('', args.port), RequestHandler)
    print("Launching example HTTP server")
    httpd.serve_forever()

if __name__ == '__main__':
    main()
