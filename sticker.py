from pyrogram import Client, Filters
import time
from pyrogram.errors import FloodWait
app = Client ("ssss",bot_token="959566620:AAFq_Rc8jlpttg3MZauPsW5yuKrApoL_x58",api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9")                                   

@app.on_message(Filters.channel)
def main(client, message):
 if message.text == "6":
  client.send_sticker(int(u),'CAADBQADHAAD271NHXPgZgboyWwDAg')
 elif message.text == "4":
  client.send_sticker(int(u),'CAADBQADGwAD271NHWpGz0fJOgEPAg')

 
app.run()
