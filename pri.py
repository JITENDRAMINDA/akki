from pyrogram import Client, Filters,Emoji
from pyrogram.errors import FloodWait
import time
app = Client("baaz",869912,"a7b049e08df35464047d57e5134327e5")
s = -1001153640657
d = -1001378725482
@app.on_message(Filters.chat(s) & Filters.text & ~Filters.edited)
def forward(client, message):
 f = False
 words = [' id','स','dekho','TRUST','fix','😱','😳','👆','👇','pass','chase','link','loss','audio','open','paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','🥺','member','only','chut','lund','gand','bhosdi','lavde','chutiya','☝️','bc','madarchod','gandu','❓','kya','line','https://','😂','🤔','LUND','WICKET LU','?','loda','telegram','chor','join']
 for word in words:
  if word.casefold() in message.text.casefold():
   f = True
 if not f:
  if "🎾" in message.text:
   mes = client.send_message(d,' '.join(message.text.split("🎾")[:-1]) + "🎾")
   files = open("sure.txt" , "a")
   files.write(" " + str(message.message_id) +  " " + str(mes.message_id))
   files.close()
  else:
   mes = client.send_message(d,message.text.replace("TRINBAGO","𝕋ℝ𝕀ℕ𝔹𝔸𝔾𝕆").replace("🖲","🙇🏼‍♂").replace("🇦🇲","🇮🇶").replace("📟","🎳").replace("🇩🇪","🇮🇶"))
   files = open("sure.txt" , "a")
   files.write(" " + str(message.message_id) +  " " + str(mes.message_id))
   files.close()  
@app.on_message(Filters.chat(s) & Filters.text & Filters.edited)
def forward(client, message):
 file = open("sure.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
  x = line.split()
  id = str(message.message_id)
  if id in x:
   try:
    if "🎾" in message.text:
     client.edit_message_text(d,int(x[x.index(id)+1]),' '.join(message.text.split("🎾")[:-1]) + "🎾" )
    else:
     client.edit_message_text(d,int(x[x.index(id)+1]),message.text.replace("TRINBAGO","𝕋ℝ𝕀ℕ𝔹𝔸𝔾𝕆").replace("🖲","🙇🏼‍♂").replace("🇦🇲","🇮🇶").replace("📟","🎳"))
   except FloodWait as e:
    time.sleep(e.x)
@app.on_deleted_messages(Filters.chat(s))
def main(client, messages):
 for v in messages:
  file = open("sure.txt" , "r")
  lines = file.readlines()
  file.close()
  for line in lines:
   x = line.split()
   id = str(v.message_id )
   if id in x:
    try:
     client.edit_message_text(d,int(x[x.index(id)+1]),".")
     client.delete_messages(d,int(x[x.index(id)+1]))
    except FloodWait as e:
     time.sleep(e.x)
@app.on_message(Filters.command("cz"))
def main(client, message):
 with open("sure.txt" , "w") as files:
  files.write("001 002")
  files.close()
  message.reply("Done") 
app.run()
