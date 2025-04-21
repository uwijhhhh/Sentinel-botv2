import discord
from discord.ext import commands
import os
import json

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Charger les cogs
@bot.event
async def on_ready():
    print(f"{bot.user.name} est connecté.")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

if __name__ == "__main__":
    with open("config.json") as f:
        config = json.load(f)
    bot.run(config["token"])
