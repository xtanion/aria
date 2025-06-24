import os
import asyncio
import websockets
from dotenv import load_dotenv
from utils.logger import get_logger

load_dotenv()
PORT = int(os.getenv("PORT", 8000)) 

logger = get_logger()

connected_clients = set()

async def handler(websocket):
    logger.info("New client connected!")
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            logger.info(f"Received: {message}")
            for client in connected_clients:
                await client.send(f"[Broadcast] {message}")
    except websockets.exceptions.ConnectionClosed:
        logger.warning("Client disconnected.")
    finally:
        connected_clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "0.0.0.0", PORT):
        logger.info(f"WebSocket started on ws://0.0.0.0:{PORT}")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
