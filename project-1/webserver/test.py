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

ws.run("", 3882)

