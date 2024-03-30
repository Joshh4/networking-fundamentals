"""wserve_test.py

This file serves as a testing grounds for WServe,
a web server experiment I created.

WServe's syntax and use of decorators was based on
that of Flask's.

wserve_test.py must be run from the working directory
/web-server-experiments/webserver/ or else it will
not run properly.
"""

import wserve

ws = wserve.WebServer()

@ws.route("/")
def root(request=None):
    return 200, "Root page"

@ws.route("/img")
def root(request=None):
    return 200, "<img src=\"relative.jpg\">"

@ws.route("/args")
def root(request=None):
    return 200, "<p>URL arguments are displayed here. Add arguments to the url with &k=v</p><ul>"+"".join([f"<li>{k} = {v}</li>" for k,v in request.args.items()])+"<ul>"

# Run web server on port 3882.
# Connect on a browser with http://localhost:3882/
ws.run("", 3882)