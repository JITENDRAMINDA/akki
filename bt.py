from pyrogram import Client, Filters
import time
from pyrogram.errors import FloodWait
k = -1001354479404
bot = "985830358:AAEWUPpF0U_Her_vLbxbylCEVCNNxhaURNU"
app = Client(session_name="rr",api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9",bot_token = bot)                                   
bullet = -1001428773103                                              
ferrari = -1001421693753                                             
@app.on_message(Filters.chat(ferrari) & ~ Filters.edited)
def main(client, message):
 mes = client.send_message( k,message.text.markdown.replace("🎾","🎾 Ball Chalu 🎾"))
 fie = open("ids.txt","a")
 fie.write(" " + str(message.message_id) + " " + str(mes.message_id))
 fie.close()
@app.on_message(Filters.chat(ferrari) & Filters.edited)
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
        client.edit_message_text(k,int(x[x.index(id)+1]),message.text.markdown.replace("🎾","🎾 Ball Chalu 🎾"))
     except FloodWait as e:
        time.sleep(e.x)
@app.on_message(Filters.chat(bullet) & ~ Filters.edited)
def main(client, message):
 mes = client.send_message( k,message.text.markdown.replace("🎾","🎾 Ball Chalu 🎾"))
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
      client.edit_message_text(k,int(x[x.index(id)+1]),message.text.markdown.replace("🎾","🎾 Ball Chalu 🎾"))
   except FloodWait as e:
     time.sleep(e.x)
@app.on_message(Filters.command('clear') & Filters.user(491634139))
def forward(client, message):
  with open("ids.txt","w") as fie:
   fie.write("001 002")
   fie.close()
   message.reply("☢️ Done, Editing data cleared ✅✅")
app.run()
