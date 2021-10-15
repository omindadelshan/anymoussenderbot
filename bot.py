from pyrogram import Client,filters

API_ID = "6021226"
API_HASH = "7c6dd7679f9dc0ab599f336de13cedf1"
TOKEN ="2092590107:AAFld-bHnflQ7Ra1RN-daiPaUuYeHC_Q_kI"

app = Client("tagremover1", bot_token = TOKEN, api_id = API_ID, api_hash = API_HASH)

@app.on_message(filters.private & filters.text | filters.media)
async def tag(client, message):
  await message.copy(message.chat.id)

app.run()
