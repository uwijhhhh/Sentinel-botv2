import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Récupérer le token depuis la variable d'environnement
TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    raise ValueError("Le token Discord n'a pas été trouvé dans les variables d'environnement.")

# Charger les cogs
@bot.event
async def on_ready():
    print(f"{bot.user.name} est connecté.")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

if __name__ == "__main__":
    bot.run(TOKEN)
