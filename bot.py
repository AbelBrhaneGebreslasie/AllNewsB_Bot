import asyncio
from telethon import TelegramClient, events

# Telegram API credentials
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

# መረጃው እንዲላክበት የምትፈልገው ቦታ (የአንተ ቦት username)
TARGET_BOT = '@AllNewsB_Bot'

client = TelegramClient('All Info', api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHATS))
async def main(event):
    try:
        await client.forward_messages(TARGET_BOT, event.message)
        print(f"New post forwarded from {event.chat_id}")
    except Exception as e:
        print(f"Error: {e}")

print("Bot is starting...")
client.start()
client.run_until_disconnected()
