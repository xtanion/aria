import asyncio
import websockets

async def send_message():
    uri = "ws://0.0.0.0:8000"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello World!")
        reply = await websocket.recv()
        print(f"Received: {reply}")

asyncio.run(send_message())
