from pyrogram import Client, Filters
import time
from pyrogram.errors import FloodWait
app = Client ("ssss",bot_token="941456512:AAGbpYo0uWZXVEgTDCfo0DtMN-GnwzC49ws",api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9")                                   
@app.on_message(Filters.channel)
def main(client, message):
 if message.text == "OVER":
  x = random.choice(1,5)
  if x == 1 :
   file = open("1.txt","r")
   s = file.readlines()
   file.close()
   client.send_message(message.chat.id,s)
  if x == 2 :
   file = open("2.txt","r")
   s = file.readlines()
   file.close()
   client.send_message(message.chat.id,s)
  if x == 3 :
   file = open("3.txt","r")
   s = file.readlines()
   file.close()
   client.send_message(message.chat.id,s)
  if x == 4 :
   file = open("4.txt","r")
   s = file.readlines()
   file.close()
   client.send_message(message.chat.id,s)
@app.on_message(Filters.command('set'))
def ran(client,message):
 x = message.from_user.id
 if x == 491634139 :
  with open("message.text.split(' ')[1].txt","w") as file:
   file.write(message.reply_to_message.text)
   file.close()
   message.reply("Done")
app.run()
@app.on_message(Filters.private & Filters.sticker)
def forawrd(client, message):
  client.send_message(message.chat.id,message.sticker.file_id )
app.run()
