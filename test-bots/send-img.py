from baleapi import Bot

TOKEN = "YOUR_BOT_TOKEN"
bot = Bot(TOKEN)

async def handle(msg):
    if msg.text == "/photo":
        url = "https://picsum.photos/300/200"  # عکس رندوم
        await bot.client.send_photo(msg.chat["id"], url, "یه عکس رندوم 📸")

bot.add_message_handler(handle)
bot.run()
