from pyrogram import Client,filters 

API_ID = "6021226" 
API_HASH = "7c6dd7679f9dc0ab599f336de13cedf1" 
TOKEN ="2092590107:AAFld-bHnflQ7Ra1RN-daiPaUuYeHC_Q_kI" 

app = Client("tagremover1", bot_token = TOKEN, api_id = API_ID, api_hash = API_HASH) 

START_TEXT = f""" **Here There Welcome To Bot Menu🤩\nThis Is A Our Bots And Projects 👇👇** """ 


@app.on_message(filters.command(["start"]))
async def start(client, message):
await message.reply_text(
  text=START_TEXT,
  disable_web_page_preview=False,
  reply_markup=START_BTN) 

app.run()
