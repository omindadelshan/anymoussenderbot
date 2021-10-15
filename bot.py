from pyrogram import Client,filters

API_ID = ""
API_HASH = ""
TOKEN =""

app = Client("tagremover1", bot_token = TOKEN, api_id = API_ID, api_hash = API_HASH)

@app.on_message(filters.private & filters.text | filters.media)
async def tag(client, message):
  await message 
  message.copy(message.chat.id)

app.run()
