from discord import Intents
from discord.ext import commands
from discord.ui import Button, View
from time import sleep
import json
from aiAnswer import generateAnswer
import os
import dotenv
dotenv.load_dotenv()

TOKEN = os.getenv("DC_TOKEN")
bot = commands.Bot(command_prefix='!', intents=Intents.all())
isSent = False

class LinkView(View):
    def __init__(self):
        super().__init__()
        # Add a button with a label and a URL
        self.add_item(Button(label="🌎Website", url="https://discord.com/"))
        self.add_item(Button(label="📜Docs", url="https://discord.com/developers/docs"))

@bot.event
async def on_message(message):
    global isSent
    certification = "Made with 💖 by HighTech"
    response_text = "No response available."
    content = str(message.content)
    if not isSent:
        if content.startswith("/ask"):
            inputData = content.removeprefix("/ask")
            response_text = generateAnswer(inputData)
            if response_text:
                try:
                    isSent = True
                    certification = "Powered by the Orange Assistant and made by Orange."
                    await message.channel.send(f"{response_text}\n\n{certification}", view=LinkView())
                except:
                    pass
        else:
            pass
    else:
        isSent = False

if __name__ == "__main__":
    bot.run(TOKEN)
