import discord
from discord.ext import commands
from discord.commands import Option, slash_command
import json
import wikipedia 


with open ('././config/guilds.json', 'r') as f:
	data = json.load(f)
	guilds = data['guilds']

with open ('././config/emotes.json', 'r') as f:
	Emotedata = json.load(f)
	

class slashWiki(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(
		description="Search any Wikipedia article",
		guild_ids=guilds
	)
	async def wikipedia(
		self, 
		ctx,
		query: Option(str, "What you want to search?", required=True)
	):
		await ctx.response.defer()
		crossEmote = Emotedata["cross"]
		infoEmote = Emotedata["info"]
	
		try:
			linkgen = wikipedia.page(query)
			link = linkgen.url
			result = wikipedia.summary(query, sentences=5)
			
			embed = discord.Embed(title=linkgen.title.upper(), description="> "+f"{result}", color=discord.Color.random())
			view = discord.ui.View()
			view.add_item(discord.ui.Button(label='Read More', url=link, style=discord.ButtonStyle.url, emoji=infoEmote))
			
			await ctx.respond(embed=embed, view=view)
		except:
			embed = discord.Embed(description=f"> {crossEmote} No result found", color=discord.Color.red())
			await ctx.respond(embed=embed)	

		
def setup(bot):
	bot.add_cog(slashWiki(bot))