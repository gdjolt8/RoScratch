import scratchattach as scratch3
import os
import requests

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
sid = "\".eJxVj8tugzAQRf-FdUvxGIzJLl1UVRaNVCJVWVl-jINLsCMwitSq_15bYpOl7xmfufNbrAvOXk5Y7AonnY9qXiIvnooYRvQpbHjTKCAMalA1UMKxy2-pWis15XbXrOpEj1-R9eFAVnTvQ39_O4pDfzonzTVcnH92t2RqoeRVCaQq6y4RIdc4iLxeOJMwS6RhAAmZb-kvQUQ34U_wudp-wtlp-fKBd3EO8_j4f5DLkKvWivIWjGltJStTM2JsR5nWpLIWiJZIgDKq8nW4RB3C6LL8noRoHpVK6nR_7pUz9DFtjy74cgNL-Ym36xa-bsN__zgpbCY:1sM9XM:JKrz5lXLYOcq41ylQucuk7faMVs\""
session = scratch3.Session(sid, username="iaintbrst8")
events = scratch3.CloudEvents("1041791800")
conn = scratch3.CloudConnection(project_id="1041791800", username="iaintbrst8", session_id=sid)
@events.event
def on_set(event): #Called when a cloud var is set
    value = str(event.value)
    decoded_value = scratch3.Encoding.decode(value)
    if event.var == "INTERACTION" and event.value == "1":
        put_value(scratch3.Encoding.encode(get_user_id(value)))
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