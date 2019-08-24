from pyrogram import Client, Filters,Emoji
from pyrogram.errors import FloodWait
import time
app = Client("session",771202,"28eed966b0cd4238a4f4f8f0ab4c9c72")
s = -1001153640657
d = -1001274887387
@app.on_message(Filters.chat(s) & Filters.text & ~Filters.edited)
def forward(client, message):
 f = False
 words = ["kab","mani"," id","स",'dekho',"TRUST",'fix','😱','😳','👆','👇','match','pass','chase','defend','karva','link','loss','audio','varna','open','paid','contact','baazigar','market','load','whatsapp','book','teen','diya','bhai',"🐴",'🥺','🖕','member','only','chut','lund','gand','ma ','maa ','bhosdi','bahan','loude','lode','lavde','chutiya','☝️','mkc','bc','madarchod','bahanchod','gandu','❓','kya','line',"https://",'bullet','🤔','LUND'," LU","?","loda","lode","lodu","telegram","chor","join"]
 for word in words:
  if word.casefold() in message.text.casefold():
   f = True
 if not f:
  mes = client.send_message(d, message.text.replace("🇩🇪","🇮🇩").replace("📟","🥁").replace("WD","WD✔️✔️").replace("LGANA","LAGANA").replace("TIME OUT ✔️✔️","🕰 TIME OUT 🕰").replace("🅿️🅰💲💲✔️✔️","🅿️🅰️💲💲🔚").replace("🕵️‍♀️","🔍").replace(" WICKET "," WICKET WICKET ").replace("🔹BOTH🔹","BOTH✔️✔️").replace("NB","NO BALL✔️✔️").replace("OVER 🖲","OVER 🧚‍♂️⛳️").replace("OVER  🖲","OVER  🧚‍♂️⛳️").replace("OVER   🖲","OVER   🧚‍♂️⛳️").replace("🖲","🧚‍♂️"))
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
    client.edit_message_text(d,int(x[x.index(id)+1]),message.text.replace("🇩🇪","🇮🇩").replace("📟","🥁").replace("WD","WD✔️✔️").replace("LGANA","LAGANA").replace("TIME OUT ✔️✔️","🕰 TIME OUT 🕰").replace("🅿️🅰💲💲✔️✔️","🅿️🅰️💲💲🔚").replace("🕵️‍♀️","🔍").replace(" WICKET "," WICKET WICKET ").replace("🔹BOTH🔹","BOTH✔️✔️").replace("NB","NO BALL✔️✔️").replace("OVER 🖲️","OVER 🧚‍♂️⛳️").replace("OVER  🖲","OVER  🧚‍♂️⛳️").replace("OVER   🖲","OVER   🧚‍♂️⛳️").replace("🖲","🧚‍♂️"))
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
     client.delete_messages(d,int(x[x.index(id)+1]))
    except FloodWait as e:
     time.sleep(e.x)
@app.on_message(Filters.command("clear"))
def main(client, message):
 with open("sure.txt" , "w") as files:
  files.write("001 002")
  files.close()
  message.reply("Done") 
app.run()
