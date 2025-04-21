import discord
from discord.ext import commands
import json
import os

CONFIG_FILE = "servers.json"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w") as f:
            json.dump({}, f)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)

class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def config(self, ctx):
        guild = ctx.guild
        config_data = load_config()

        # Création du rôle Modérateur
        role = discord.utils.get(guild.roles, name="Modérateur")
        if not role:
            role = await guild.create_role(name="Modérateur", permissions=discord.Permissions(administrator=True))

        # Création de la catégorie TICKETS
        category = discord.utils.get(guild.categories, name="TICKETS")
        if not category:
            category = await guild.create_category(name="TICKETS")

        # Création du canal log
        log_channel = discord.utils.get(guild.text_channels, name="logs")
        if not log_channel:
            log_channel = await guild.create_text_channel("logs")

        # Sauvegarde dans servers.json
        config_data[str(guild.id)] = {
            "ticket_category_id": category.id,
            "log_channel_id": log_channel.id,
            "moderator_role_id": role.id
        }
        save_config(config_data)

        # Confirmation
        await ctx.send(embed=discord.Embed(
            title="Configuration terminée",
            description="Le bot est maintenant prêt à fonctionner sur ce serveur !",
            color=discord.Color.green()
        ))

async def setup(bot):
    await bot.add_cog(Config(bot))
