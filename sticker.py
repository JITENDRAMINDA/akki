from pyrogram import Client, Filters
import time
from pyrogram.errors import FloodWait
app = Client ("ssss",bot_token="790494538:AAHEtFqb6yxTGIjjcQ3O4JCYOtlhS1hU8oQ",api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9")                                   

@app.on_message(Filters.channel)
def main(client, message):
 if message.text == "6":
  c
