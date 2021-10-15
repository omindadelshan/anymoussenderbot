from pyrogram import Client,filters

API_ID = "6021226"
API_HASH = "7c6dd7679f9dc0ab599f336de13cedf1"
TOKEN ="2092590107:AAFld-bHnflQ7Ra1RN-daiPaUuYeHC_Q_kI"

app = Client("tagremover1", bot_token = TOKEN, api_id = API_ID, api_hash = API_HASH)

START_TXT = "Hi Bro bay"

@app.on_message(filters.private & filters.text | filters.media)
async def tag(client, message):
  await message.copy(message.chat.id)
  
@app.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TXT.format(update.from_user.mention)
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

app.run()
