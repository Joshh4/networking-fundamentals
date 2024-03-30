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
renderer = wserve.BirchRenderer()

renderer.set_global_scope_entry("example_value", "This string is inside of Birch global scope!")

@ws.route("/")
def page_root(request:wserve.HTMLRequest):
    return 200, "Root page"

@ws.route("/img")
def page_img(request:wserve.HTMLRequest):
    return 200, "<img src=\"relative.jpg\">"

@ws.route("/args")
def page_args(request:wserve.HTMLRequest):
    return 200, "<p>URL arguments are displayed here. Add arguments to the url with &k=v</p><ul>"+"".join([f"<li>{k} = {v}</li>" for k,v in request.args.items()])+"<ul>"

@ws.route("/birch")
def page_birch(request:wserve.HTMLRequest):
    return 200, renderer.render("birch.html", example_value="replaced")

# Import threading for the reason(s) below...
import threading, time

# Use threading to run web server on port 3882.
# ( Connect on a browser with http://localhost:3882/ )

# Threading allows the user to quit the server
# using CTRL+C.

threading._start_new_thread(ws.run, ("", 3882))

print("Running WebServer on port 3882")

while True:
    # Respond to KeyboardInterrupt
    time.sleep(0.5)
