import scratchattach as scratch3
import os
import requests
import http.server
import socketserver
def get_user_id(username):
    url = f"https://users.roblox.com/v1/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None
def put_value(var):
    print(f"Compresing: {var}")
    for i in range(0, round(len(var)/256)):
        print(var[(i * 256):(i * 256 + 256)])
        conn.set_var(f"CLOUD{i}", var[(i * 256):(i * 256 + 256)])
sid = os.environ["TOK"]
session = scratch3.Session(sid, username="iaintbrst8")
events = scratch3.CloudEvents("1041791800")
conn = scratch3.CloudConnection(project_id="1041791800", username="iaintbrst8", session_id=sid)
@events.event
def on_set(event): #Called when a cloud var is set
    value = str(event.value)
    decoded_value = scratch3.Encoding.decode(value)
    if event.var == "INTERACTION" and event.value == "1":
        val = get_user_id(value)
        arr = val['description'] + ";" + str(val['created']) + ";" + str(val['isBanned']) + ";" + val['name'] + ';' + val['displayName']
        put_value(scratch3.Encoding.encode(arr))
        conn.set_var("INTERACTION", 0)

@events.event
def on_del(event):
    print(f"{event.user} deleted variable {event.var}")

@events.event
def on_create(event):
    print(f"{event.user} created variable {event.var}")

@events.event #Called when the event listener is ready
def on_ready():
   print("Event listener ready!")

events.start()
PORT = 8000

class HelloWorldHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Set the response status code to 200 (OK)
        self.send_response(200)
        # Set the headers
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Write the response content
        self.wfile.write(b"Hello, World!")

with socketserver.TCPServer(("", PORT), HelloWorldHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
