import asyncio
import os
from rubika_bot_api.api import Robot
from rubika_bot_api import filters

TOKEN = os.getenv("RUBIKA_TOKEN")
if not TOKEN:
    raise RuntimeError("RUBIKA_TOKEN is not set")

bot = Robot(token=TOKEN)

@bot.on_message(filters=filters.pv & filters.text)
async def auto_reply(bot_instance, message):
    text = (message.text or "").strip()
    if text == "/start":
        answer = "سلام! ربات فعاله. پیام خودت رو بفرست."
    else:
        answer = f"پیامت دریافت شد: {text}"
    await message.reply(answer)

if __name__ == "__main__":
    asyncio.run(bot.run())
