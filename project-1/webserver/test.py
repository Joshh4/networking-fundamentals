import wserve

ws = wserve.WebServer()

@ws.route("/")
def root(req=None):
    return 200, "Root page"

ws.run("", 3882)