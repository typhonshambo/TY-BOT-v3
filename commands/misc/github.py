import aiohttp
import discord
from discord.ext import commands
from discord.commands import Option, slash_command, SlashCommandGroup
import json

with open ('././config/guilds.json', 'r') as f:
	data = json.load(f)
	guilds = data['guilds']

with open ('././config/api.json', 'r') as f:
	ApiData = json.load(f)
	githubApi = ApiData['github']
	

class slashGithub(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(description="Search any github user", guild_ids=guilds)
	async def github(
		self, 
		ctx,
		username: Option(str, "Enter Github Username", required=True)
	):

		await ctx.response.defer()
		url = str(githubApi)+ str(username)

		async with aiohttp.ClientSession() as session:
			async with session.get(url) as r:
				r = await r.json()

			try:
				username = r["login"]
				avatar = r["avatar_url"]
				githuburl = r["html_url"]
				name = r["name"]
				location = r["location"]
				email = r["email"]
				company = r["company"]
				bio = r["bio"]
				repo = r["public_repos"]

				embed = discord.Embed(
					colour=0x00FFFF,
					title=f"Github Profile",
					description=f"""
						> `Github username` : {username}
						> `Github link` : {githuburl}
						> `Name` : {name}
						> `Location` : {location}
						> `Email` : {email}
						> `Company` : {company}
						> `Bio` : {bio}
						> `Repository` : {repo}
					""")

				embed.set_thumbnail(url=avatar)
				await ctx.respond(embed=embed)

				

			except:
				embed = discord.Embed(
					colour=0x983925,
					description=f">  ⚠️Unable to find the github profile please check your spelling",
				)
				await ctx.respond(embed=embed)
				

def setup(bot):
	bot.add_cog(slashGithub(bot))