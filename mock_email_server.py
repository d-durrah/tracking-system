import asyncio
from aiosmtpd.controller import Controller
import logging

logging.basicConfig(filename='email.log', level=logging.DEBUG)

class MockEmailServer:
    def __init__(self, host='localhost', port=1025):
        self.host = host
        self.port = port

    async def start(self):
        self.controller = Controller(self.handle_message, hostname=self.host, port=self.port)
        self.controller.start()

    async def stop(self):
        self.controller.stop()

    async def handle_message(self, message):
        envelope = message.envelope
        logging.debug(f"Received message from {envelope.rcpt_tos} with content:\n{message}")

async def main():
    server = MockEmailServer()
    await server.start()
    try:
        await asyncio.sleep(86400)  # Run for one day
    finally:
        await server.stop()

if __name__ == '__main__':
    asyncio.run(main())