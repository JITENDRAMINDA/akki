from pyrogram import Client, Filters
import time
from pyrogram.errors import FloodWait
app = Client ("ssss",bot_token="959566620:AAGdt9-HIPcefOmfIrIZNSRc8vuqg_UVxgM",api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9")                                   

@app.on_message(Filters.channel)
def main(client, message):
 if message.text == "6":
  client.send_sticker(message.chat.id,'CAADBQADNwADy-MGFaBs2toKhjOuAg')
 elif message.text == "4":
  client.send_sticker(message.chat.id,'CAADBQADOAADy-MGFcTomafSvj85Ag')
 elif "WICKET" in message.text:
  client.send_sticker(message.chat.id,'CAADBQADNwADy-MGFaBs2toKhjOuAg')
 elif 'DRINKS BREAK' in message.text:
  client.send_sticker(message.chat.id,'CAADBQADRgADy-MGFUpRV_38qCywAg')
 elif 'WIDE' in message.text:
  client.send_sticker(message.chat.id,'CAADBQADQQADy-MGFbOcRX3V6UQ6Ag')
 elif 'DEAD BALL' in message.text:
  client.send_sticker(message.chat.id,'CAADBQADPQADy-MGFdWUWIDhSc-DAg')
 elif 'NB' in message.text:
  client.send_sticker(message.chat.id,'CAADBQADOQADy-MGFW3th7obf0AiAg')
 elif 'CLOSING' in message.text:
  client.send_sticker(message.chat.id,'CAADBQADRwADy-MGFb1ffrrgFbgbAg')
 

@app.on_message(Filters.private & Filters.sticker)
def forawrd(client, message):
  client.send_message(message.chat.id,message.sticker.file_id )


app.run()
