import aiohttp
import discord
from discord.ext import commands
from discord.commands import Option, slash_command, SlashCommandGroup
import json

with open ('././config/guilds.json', 'r') as f:
	data = json.load(f)
	guilds = data['guilds']

with open ('././config/emotes.json', 'r') as f:
	Emotedata = json.load(f)


class slashAnime(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	anime = SlashCommandGroup(
		"anime",
		"Generate a Anime image",
		guild_ids=guilds
	) #;-; i have not added any permissions here


	@anime.command(description="Feed a member")
	async def feed(
		self, 
		ctx, 
		member: Option(discord.Member, "Mention a user",required=False)
	):
		await ctx.response.defer()
		async with aiohttp.ClientSession() as session:
			async with session.get("https://nekos.life/api/v2/img/feed") as r:
				r = await r.json()
				url = r["url"]

				embed = discord.Embed(colour=0xFC7EF5, title="feed")
				embed.set_image(url=url)
				embed.set_footer(text=f"┗Requested by {ctx.author}")


				embed2 = discord.Embed(description=f"> {ctx.author.mention} fed {member.mention}",colour=0xFC7EF5, title="feed")
				embed2.set_image(url=url)
				embed2.set_footer(text=f"┗Requested by {ctx.author}")
				
				if member is None:
					await ctx.respond(embed=embed)
				else:
					await ctx.respond(embed=embed2)


	@anime.command(description="tickle a member")
	async def tickle(
		self, 
		ctx, 
		member: Option(discord.Member, "Mention a user",required=False)
	):
		await ctx.response.defer()
		async with aiohttp.ClientSession() as session:
			async with session.get("https://nekos.life/api/v2/img/tickle") as r:
				r = await r.json()
				url = r["url"]

				embed = discord.Embed(colour=0xFC7EF5, title="tickle")
				embed.set_image(url=url)
				embed.set_footer(text=f"┗Requested by {ctx.author}")


				embed2 = discord.Embed(description=f"> {ctx.author.mention} fed {member.mention}",colour=0xFC7EF5, title="tickle")
				embed2.set_image(url=url)
				embed2.set_footer(text=f"┗Requested by {ctx.author}")
				
				if member is None:
					await ctx.respond(embed=embed)
				else:
					await ctx.respond(embed=embed2)

	@anime.command(description="slap a member")
	async def slap(
		self, 
		ctx, 
		member: Option(discord.Member, "Mention a user",required=False)
	):
		await ctx.response.defer()
		async with aiohttp.ClientSession() as session:
			async with session.get("https://nekos.life/api/v2/img/slap") as r:
				r = await r.json()
				url = r["url"]

				embed = discord.Embed(colour=0xFC7EF5, title="slap")
				embed.set_image(url=url)
				embed.set_footer(text=f"┗Requested by {ctx.author}")


				embed2 = discord.Embed(description=f"> {ctx.author.mention} fed {member.mention}",colour=0xFC7EF5, title="slap")
				embed2.set_image(url=url)
				embed2.set_footer(text=f"┗Requested by {ctx.author}")
				
				if member is None:
					await ctx.respond(embed=embed)
				else:
					await ctx.respond(embed=embed2)


	@anime.command(description="hug a member")
	async def hug(
		self, 
		ctx, 
		member: Option(discord.Member, "Mention a user",required=False)
	):
		await ctx.response.defer()
		async with aiohttp.ClientSession() as session:
			async with session.get("https://nekos.life/api/v2/img/hug") as r:
				r = await r.json()
				url = r["url"]

				embed = discord.Embed(colour=0xFC7EF5, title="hug")
				embed.set_image(url=url)
				embed.set_footer(text=f"┗Requested by {ctx.author}")


				embed2 = discord.Embed(description=f"> {ctx.author.mention} fed {member.mention}",colour=0xFC7EF5, title="hug")
				embed2.set_image(url=url)
				embed2.set_footer(text=f"┗Requested by {ctx.author}")
				
				if member is None:
					await ctx.respond(embed=embed)
				else:
					await ctx.respond(embed=embed2)
					
				
	@anime.command(description="smug a member")
	async def smug(
		self, 
		ctx, 
		member: Option(discord.Member, "Mention a user",required=False)
	):
		await ctx.response.defer()
		async with aiohttp.ClientSession() as session:
			async with session.get("https://nekos.life/api/v2/img/smug") as r:
				r = await r.json()
				url = r["url"]

				embed = discord.Embed(colour=0xFC7EF5, title="smug")
				embed.set_image(url=url)
				embed.set_footer(text=f"┗Requested by {ctx.author}")


				embed2 = discord.Embed(description=f"> {ctx.author.mention} fed {member.mention}",colour=0xFC7EF5, title="smug")
				embed2.set_image(url=url)
				embed2.set_footer(text=f"┗Requested by {ctx.author}")
				
				if member is None:
					await ctx.respond(embed=embed)
				else:
					await ctx.respond(embed=embed2)


	@anime.command(description="kiss a member")
	async def kiss(
		self, 
		ctx, 
		member: Option(discord.Member, "Mention a user",required=False)
	):
		await ctx.response.defer()
		async with aiohttp.ClientSession() as session:
			async with session.get("https://nekos.life/api/v2/img/kiss") as r:
				r = await r.json()
				url = r["url"]

				embed = discord.Embed(colour=0xFC7EF5, title="kiss")
				embed.set_image(url=url)
				embed.set_footer(text=f"┗Requested by {ctx.author}")


				embed2 = discord.Embed(description=f"> {ctx.author.mention} fed {member.mention}",colour=0xFC7EF5, title="kiss")
				embed2.set_image(url=url)
				embed2.set_footer(text=f"┗Requested by {ctx.author}")
				
				if member is None:
					await ctx.respond(embed=embed)
				else:
					await ctx.respond(embed=embed2)


	@anime.command(description="pat a member")
	async def pat(
		self, 
		ctx, 
		member: Option(discord.Member, "Mention a user",required=False)
	):
		await ctx.response.defer()
		async with aiohttp.ClientSession() as session:
			async with session.get("https://nekos.life/api/v2/img/pat") as r:
				r = await r.json()
				url = r["url"]

				embed = discord.Embed(colour=0xFC7EF5, title="pat")
				embed.set_image(url=url)
				embed.set_footer(text=f"┗Requested by {ctx.author}")


				embed2 = discord.Embed(description=f"> {ctx.author.mention} fed {member.mention}",colour=0xFC7EF5, title="pat")
				embed2.set_image(url=url)
				embed2.set_footer(text=f"┗Requested by {ctx.author}")
				
				if member is None:
					await ctx.respond(embed=embed)
				else:
					await ctx.respond(embed=embed2)

def setup(bot):
	bot.add_cog(slashAnime(bot))