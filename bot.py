import os
import asyncio
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
from telethon import TelegramClient, events

# 1. Dummy Web Server for Render Port Check
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

threading.Thread(target=run_http_server, daemon=True).start()

# 2. Telegram UserBot Configuration
api_id = 32062895
api_hash = 'eb0716c82a6190150c87924f55c1f087'
TARGET_BOT = '@AllNewsB_Bot'

client = TelegramClient('bot_session', api_id, api_hash)

# Listen to ALL incoming messages without chat restriction to test instantly
@client.on(events.NewMessage)
async def main(event):
    try:
        # Avoid forwarding messages sent by the bot itself or to itself in saved messages
        if event.is_private and not event.out:
            return
        
        await client.forward_messages(TARGET_BOT, event.message)
        print(f"Forwarded message from chat: {event.chat_id}")
    except Exception as e:
        print(f"Error forwarding message: {e}")

print("UserBot is starting and listening to all chats...")
client.start()
print("UserBot is running successfully!")
client.run_until_disconnected()
