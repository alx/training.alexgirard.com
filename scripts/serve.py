#!/usr/bin/env python3
"""Static preview server for training.alexgirard.com (port 8091).

Like `python3 -m http.server` but adds charset=utf-8 to text/* responses —
plain http.server sends e.g. `Content-type: text/plain` with no charset,
which makes UTF-8 files (llms.txt, robots.txt…) render mangled in
charset-guessing clients.

Usage: serve.py [port] [directory]
"""
import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class Handler(SimpleHTTPRequestHandler):
    def send_header(self, key, value):
        if key.lower() == "content-type" and value.startswith("text/") and "charset" not in value:
            value += "; charset=utf-8"
        super().send_header(key, value)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8091
    directory = sys.argv[2] if len(sys.argv) > 2 else "public"
    handler = partial(Handler, directory=directory)
    server = ThreadingHTTPServer(("0.0.0.0", port), handler)
    print(f"serving {directory} on 0.0.0.0:{port}", file=sys.stderr)
    server.serve_forever()
