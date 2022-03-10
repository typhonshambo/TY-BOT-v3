import discord
from discord.ext import commands
from discord.commands import Option, slash_command
import json

with open ('././config/guilds.json', 'r') as f:
	data = json.load(f)
	guilds = data['guilds']

class slashPing(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
 
	@commands.slash_command(
		description="sends latency of BOT",
        guild_ids=guilds
	)
	async def ping(self, ctx):
		_ping = int(round(self.bot.latency * 1000))
		
		embed = discord.Embed(
			title = f'Latency = {_ping} ms',
			color = discord.Color.blue()
		)
		await ctx.respond(embed=embed)

def setup(bot):
	bot.add_cog(slashPing(bot))
