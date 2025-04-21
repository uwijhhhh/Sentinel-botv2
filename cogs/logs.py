import discord
from discord.ext import commands

class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        log_channel_id = self.get_config(guild.id, "log_channel_id")
        log_channel = discord.utils.get(guild.text_channels, id=log_channel_id)
        if log_channel:
            await log_channel.send(f"{user} a été banni du serveur.")

    def get_config(self, guild_id, key):
        with open("servers.json") as f:
            data = json.load(f)
        return data.get(str(guild_id), {}).get(key)

async def setup(bot):
    await bot.add_cog(Logs(bot))
