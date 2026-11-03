import os
import asyncio
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
from telethon import TelegramClient, events

# 1. Dummy Web Server for Render Port Check (Supports GET and HEAD)
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running 24/7!")

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

def run_http_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

# Start HTTP Server in background thread
threading.Thread(target=run_http_server, daemon=True).start()

# 2. Telegram UserBot Configuration
api_id = 32062895
api_hash = 'eb0716c82a6190150c87924f55c1f087'

# የምትከታተላቸው ቻናሎች እና ግሩፖች
SOURCE_CHATS = [
    '@aastuvwgeologia',
    '@Aastu_poll',
    '@truthwithrose4930',
    '@aastusu2012',
    '@pir2011',
    '@aastu_confessions',
    '@Ethio_Aviators',
    '@AASTU_Registrar',
    -1003909358640,
    -1004354555692,
    -1003234571340
]

TARGET_BOT = '@AllNewsB_Bot'

# Loads 'bot_session.session' directly
client = TelegramClient('bot_session', api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHATS))
async def main(event):
    try:
        await client.forward_messages(TARGET_BOT, event.message)
        print(f"New post forwarded from {event.chat_id}")
    except Exception as e:
        print(f"Error forwarding message: {e}")

print("UserBot is starting...")

# Start client using the uploaded session file (No token, no phone prompt needed)
client.start()
print("UserBot is running successfully and listening to channels!")
client.run_until_disconnected()
