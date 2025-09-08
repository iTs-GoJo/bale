from baleapi import Bot

TOKEN = "YOUR_BOT_TOKEN"
bot = Bot(TOKEN)

async def handle(msg):
    if msg.text == "/start":
        await bot.client.send_message(msg.chat["id"], "سلام 😎 خوش اومدی به ربات من!")

bot.add_message_handler(handle)
bot.run()
