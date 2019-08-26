from pyrogram import Client, Filters
import time
app = Client ("ssss",bot_token="944635483:AAGJ1AhIaRP4BQagRlU5gYThgWAhrQydSy0",api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9")                                   

@app.on_message(Filters.channel)
def main(client, message):
 file = open("sure.txt" , "r")
 lines = file.readlines()
 file.close()
 for b in lines:
  if b == "atv":
   client.delete_messages(message.chat.id, message.message_id)
@app.on_message(Filters.command("atv"))
def main(client, message):
 with open("sure.txt" , "w") as files:
  files.write("atv")
  files.close()
  message.reply("okk, ab me message bhejane wali ki maa chodta tu soja")

@app.on_message(Filters.command("dtv"))
def main(client, message):
 with open("sure.txt" , "w") as files:
  files.write("dtv")
  files.close()
  message.reply("okk, ab tu message bhejane wali ki maa chod me rest krta")

app.run()
