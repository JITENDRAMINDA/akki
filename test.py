from pyrogram import Client, Filters
import time
from pyrogram.errors import FloodWait
app = Client ("ssss",bot_token="828263688:AAG03-wIxsNrmczhOHnBHaghXnEP3csfDl8",api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9")                                   
bullet = -1001203491308                                                                                           
k = -1001315425757
@app.on_message(Filters.chat(bullet) & ~ Filters.edited)
def main(client, message):
 mes = client.send_message( ' '.join(message.text.split("🎾")[:-1])))
 fie = open("ids.txt","a")
 fie.write(" " + str(message.message_id) + " " + str(mes.message_id))
 fie.close()
@app.on_message(Filters.chat(bullet) & Filters.edited)
def main(client, message):
 files = open("ids.txt" , "r")
 d = files.readlines()
 files.close()
 for c in d:
  x = c.split()
  id = str(message.message_id)
  if id in x:
   try:
     if message.text == ".":   
      client.delete_messages(k,int(x[x.index(id)+1]))
     else:
      client.edit_message_text(k,int(x[x.index(id)+1]),message.text)
   except FloodWait as e:
     time.sleep(e.x)
app.run()
