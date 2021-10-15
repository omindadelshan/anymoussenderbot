from pyrogram import Client,filters 

API_ID = "" 
API_HASH = "" 
TOKEN ="" 

app = Client("tagremover1", bot_token = TOKEN, api_id = API_ID, api_hash = API_HASH) 

START_TEXT = f""" **Here There Welcome To Bot Menu🤩\nThis Is A Our Bots And Projects 👇👇** """ 


@app.on_message(filters.command(["start"]))
async def start(client, message):
await message.reply_text(
  text=START_TEXT,
  disable_web_page_preview=False,
  reply_markup=START_BTN) 

app.run()