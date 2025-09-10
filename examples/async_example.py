import asyncio
from wolflive import WolfClient

async def main():
    client = WolfClient()
    await client.connect(token="YOUR_TOKEN")

    @client.on("message")
    async def on_msg(data):
        print("Received async:", data)

    auth = await client.login("username", "password")
    print("Logged in:", auth)

    await client.send_message("channel1", "Hello async world!")
    await client.close()

asyncio.run(main())
