import discord
from discord.ext import commands
from discord.commands import Option, slash_command
import json
from urllib.parse import quote_plus

with open ('././config/guilds.json', 'r') as f:
	data = json.load(f)
	guilds = data['guilds']

with open ('././config/emotes.json', 'r') as f:
	Emotedata = json.load(f)
	
class Google(discord.ui.View):
	def __init__(self, query: str):
		super().__init__()
		query = quote_plus(query)
		url = f"https://www.google.com/search?q={query}"

		self.add_item(discord.ui.Button(label="Click Here", url=url))


class slashGoogle(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@slash_command(
		description="Make a Google Search",
		guild_ids=guilds
	)
	async def google(
		self, 
		ctx, 
		query: Option(str, "What you want to search?", required=True)
	):
		await ctx.respond(f"Google Result for `{query}`", view=Google(query))

def setup(bot):
	bot.add_cog(slashGoogle(bot))