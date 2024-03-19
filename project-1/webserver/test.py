import wserve

ws = wserve.WebServer()

@ws.route("/")
def root(request=None):
    return 200, "Root page"

@ws.route("/img")
def root(request=None):
    return 200, "<img src=\"relative.png\">"

"""
TODO: support image loading
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36
sec-ch-ua-platform: "Windows"
Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8   <---- This line is important. Look for anything that accepts image/* then look for img src
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: no-cors
"""

@ws.route("/args")
def root(request=None):
    return 200, "<p>URL arguments are displayed here. Add arguments to the url with &k=v</p><ul>"+"".join([f"<li>{k} = {v}</li>" for k,v in request.args.items()])+"<ul>"

ws.run("", 3882)

