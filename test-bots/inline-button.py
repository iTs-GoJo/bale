from baleapi.bot import Bot
from baleapi.keyboard import Keyboard

bot = Bot("TOKEN")

async def link_demo(message, args):
    keyboard = Keyboard.inline([
        [{"text": "گیتهاب سازنده", "url": "https://github.com/iTs-GoJo/bale"}]
    ])
    await message.reply("لینک ریپو گیتهاب:", reply_markup=keyboard)

bot.add_command_handler("start", link_demo)
bot.run()
