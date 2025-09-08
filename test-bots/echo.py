from baleapi import Bot

TOKEN = "YOUR_BOT_TOKEN"
bot = Bot(TOKEN)

async def handle(msg):
    if msg.text:
        await bot.client.send_message(msg.chat["id"], f"تو گفتی: {msg.text}")

bot.add_message_handler(handle)
bot.run()
