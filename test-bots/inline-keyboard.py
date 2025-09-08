from baleapi import Bot, Keyboard

TOKEN = "YOUR_BOT_TOKEN"
bot = Bot(TOKEN)

async def handle(msg):
    if msg.text == "/menu":
        kb = Keyboard.inline([
            [{"text": "📷 عکس", "callback_data": "photo"}],
            [{"text": "ℹ️ درباره", "callback_data": "about"}]
        ])
        await bot.client.send_message(msg.chat["id"], "یه گزینه انتخاب کن:", reply_markup=kb)

bot.add_message_handler(handle)
bot.run()
