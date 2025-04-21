import discord
from discord.ext import commands
import json

class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def create_ticket(self, ctx):
        category_id = self.get_config(ctx.guild.id, "ticket_category_id")
        if category_id:
            category = discord.utils.get(ctx.guild.categories, id=category_id)
            if category:
                ticket_channel = await ctx.guild.create_text_channel(f"ticket-{ctx.author.name}", category=category)
                await ticket_channel.set_permissions(ctx.guild.default_role, read_messages=False)
                await ticket_channel.set_permissions(ctx.author, read_messages=True)
                await ticket_channel.send(f"{ctx.author.mention}, votre ticket a été créé.")
            else:
                await ctx.send("La catégorie des tickets n'a pas été trouvée.")
        else:
            await ctx.send("Le serveur n'a pas été configuré pour les tickets.")

    @commands.command()
    async def close_ticket(self, ctx):
        if ctx.channel.name.startswith("ticket-"):
            await ctx.channel.delete()
            await ctx.send("Le ticket a été fermé.")

    def get_config(self, guild_id, key):
        with open("servers.json") as f:
            data = json.load(f)
        return data.get(str(guild_id), {}).get(key)

async def setup(bot):
    await bot.add_cog(Ticket(bot))
