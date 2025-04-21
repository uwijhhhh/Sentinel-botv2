import discord
from discord.ext import commands
import os

# Création du bot avec les intents nécessaires
intents = discord.Intents.default()
intents.message_content = True  # Activer le message content

bot = commands.Bot(command_prefix="!", intents=intents)

# Récupérer le token depuis la variable d'environnement définie sur Render
TOKEN = os.getenv("DISCORD_TOKEN")

# Vérifier que le token a bien été récupéré
if TOKEN is None:
    raise ValueError("Le token Discord n'a pas été trouvé dans les variables d'environnement.")

# Charger les cogs (modules supplémentaires)
@bot.event
async def on_ready():
    print(f"{bot.user.name} est connecté.")
    # Charger tous les cogs du dossier cogs
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

# Démarrer le bot
if __name__ == "__main__":
    bot.run(TOKEN)
