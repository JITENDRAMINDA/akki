from pyrogram import Client, Filters
import time
from pyrogram.errors import FloodWait
app = Client ("ssss",bot_token="930207168:AAHEUI6NMdETxUJe9hfYR1P4BN-n5VRMKHY",api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9")                                   

@app.on_message(Filters.channel)
def main(client, message):
 if message.text == "6":
  client.send_sticker(message.chat.id,'CAADBQADOgIAApvFRx_Vb9xZ2tDZeAI')
 elif message.text == "4":
  client.send_sticker(message.chat.id,'CAADBQADOQIAApvFRx-X3zKjUZBD-AI')
 elif "WICKET" in message.text:
  client.send_sticker(message.chat.id,'CAADBQADOwIAApvFRx-9TLj8euFGYwI')
 elif 'DRINKS BREAK' in message.text:
  client.send_sticker(message.chat.id,'CAADBQADJQAD271NHRSHuFn7xmbvAg')
 elif 'WIDE' in message.text:
  client.send_sticker(message.chat.id,'CAADBQADQQIAApvFRx-ATGFrOeEkHwI')
 elif 'DEAD BALL' in message.text:
  client.send_sticker(message.chat.id,'CAADBQADPAIAApvFRx_d_0_aLMZ0CwI')
 elif 'NB' in message.text:
  client.send_sticker(message.chat.id,'CAADBQADPAIAApvFRx_d_0_aLMZ0CwI')
 elif 'CLOSING' in message.text:
  client.send_sticker(message.chat.id,'CAADBQADPgIAApvFRx9uJ-Thu3QeQQI')
 elif 'WD' in message.text:
  client.send_sticker(message.chat.id,'CAADBQADQQIAApvFRx-ATGFrOeEkHwI')
 elif "WKT" in message.text:
  client.send_sticker(message.chat.id,'CAADBQADOwIAApvFRx-9TLj8euFGYwI')
@app.on_message(Filters.private & Filters.sticker)
def forawrd(client, message):
  client.send_message(message.chat.id,message.sticker.file_id )
app.run()
