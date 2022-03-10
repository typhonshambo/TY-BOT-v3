import discord
from discord.ext import commands
from discord.commands import Option, slash_command, SlashCommandGroup
import json

with open ('././config/guilds.json', 'r') as f:
	data = json.load(f)
	guilds = data['guilds']

class avatar(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
 
	@commands.slash_command(
		description="sends avatar of any user",
		guild_ids=guilds
	)
	
	async def avatar(self, ctx, member: Option(discord.Member, "Mention a user",required=False, default=None)):
		if member == None :
			member= ctx.author
			embed= discord.Embed(title='User Avatar:' , color=0x02FCCF,url=f"{member.avatar.url}")
			embed.set_author(name=f"{member}", icon_url=f"{member.avatar.url}")
			embed.set_image(url=f'{member.avatar.url}')
			await ctx.respond(embed=embed)
		else:
			embed= discord.Embed(title='User Avatar:' , color=0x02FCCF,url=f"{member.avatar.url}")
			embed.set_author(name=f"{member}", icon_url=f"{member.avatar.url}")
			embed.set_image(url=f'{member.avatar.url}')
			embed.set_footer(text=f'Requested By {ctx.author}', icon_url=f'{ctx.author.avatar.url}')
			await ctx.respond(embed=embed)
def setup(bot):
	bot.add_cog(avatar(bot))
