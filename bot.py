from highrise import BaseBot
from highrise.models import SessionMetadata, User
from asyncio import run as arun
from highrise.__main__ import main

import os

class Bot(BaseBot):

    async def on_start(self, session_metadata: SessionMetadata):
        print("Bot Online")

    async def on_user_join(self, user: User, position):
        await self.highrise.chat(f"خوش اومدی {user.username} 🌹")

    async def run(self):
        room_id = os.getenv("ROOM_ID")
        token = os.getenv("TOKEN")
        await main(self, room_id, token)

if __name__ == "__main__":
    arun(Bot().run())
