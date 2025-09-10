from wolflive import WolfClientSync

client = WolfClientSync()
client.connect(token="YOUR_TOKEN")

def on_msg(data):
    print("Received sync:", data)

client.on("message", on_msg)
auth = client.login("username", "password")
print("Logged in:", auth)
client.sendMessage("channel1", "Hello sync world!")
