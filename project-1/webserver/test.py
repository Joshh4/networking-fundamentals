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
    return 200, renderer.render("birch.html")

print("Running WebServer on port 3882")

import threading, time
threading._start_new_thread(ws.run, ("", 3882))

while True:
    # Respond to KeyboardInterrupt
    time.sleep(0.5)