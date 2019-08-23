from pyrogram import Client, Filters
app = Client("mcc",715451,"d2cba6f7bf5d1a45682da5bb9071a307")
s = -1001262096355
d = -1001345217209
@app.on_message(Filters.chat(s) & Filters.text & ~Filters.edited)
def forward(client, message):
