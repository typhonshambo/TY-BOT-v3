import discord
from discord.ext import commands
from discord.commands import Option, slash_command
from discord.commands import CommandPermission, SlashCommandGroup
import json
from re import compile

with open ('././config/guilds.json', 'r') as f:
	data = json.load(f)
	guilds = data['guilds']

class slashTags(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	tag = SlashCommandGroup(
		"tag",
		"manage Tags",
		guild_ids=guilds
	) #;-; i have not added any permissions here

	@tag.command(description="Create a tag")
	async def create(
		self,
		ctx,
		name: Option(str, "Enter the tag name", required=True),
		content: Option(str, "Enter the Content of the tag", required=True)
	):
		await ctx.response.defer()
		guildId = ctx.guild.id
		checkTag = await self.bot.pg_con.fetchrow("SELECT * FROM tags WHERE tag_name = $1 AND guildId = $2", name, str(guildId))

		
		if not checkTag:
			await self.bot.pg_con.execute("INSERT INTO tags (guildId, tag_name , content) VALUES ($1, $2, $3)", str(guildId), name, content)
			embed = discord.Embed(
				color = discord.Color.random(),
				description=f"> Tag Created! with name `{name}`"
			)
			await ctx.respond(embed=embed)

		else:
			embed = discord.Embed(
				color = discord.Color.random(),
				description="> A tag already exist with that name\nTry any other name or edit the current one"
			)
			await ctx.respond(embed=embed)


	@tag.command(description="Show the tag")
	async def show(
		self,
		ctx,
		name: Option(str, "Enter the tag name", required=True)
	):
		await ctx.response.defer()
		guildId = int(ctx.guild.id)
		checkTag = await self.bot.pg_con.fetchrow("SELECT * FROM tags WHERE tag_name = $1 AND guildId = $2", name, str(guildId))

		if not checkTag:
			embed = discord.Embed(
				color = discord.Color.random(),
				description="> No tag found with that name!"
			)
			await ctx.respond(embed=embed)
		else:
			content = checkTag["content"]
			embed = discord.Embed(
				color = discord.Color.random(),
			)
			embed.add_field(name=name, value="> "+content)
			await ctx.respond(embed=embed)

	@tag.command(description="Show list of tags")
	async def tags(self, ctx):
		await ctx.response.defer()
		
		totalTags = await self.bot.pg_con.fetch("SELECT tag_name FROM tags")
		print(totalTags)
		
		Taglist = []
		for item in totalTags:
			Taglist.append(item[0])
		

		description="".join(f"`{str(e)}` " for e in Taglist)
		

			
		embed = discord.Embed(
			color = discord.Color.random(),
			title ="TAGS",
			description="> "+description
		)
		await ctx.respond(embed=embed)


	@tag.command(description="Show list of tags")
	async def delete(
		self, 
		ctx,
		tag: Option(str, "Enter the tag name", required=True)
	):
		await ctx.response.defer()
		guildId = int(ctx.guild.id)
		checkTag = await self.bot.pg_con.fetchrow("SELECT * FROM tags WHERE tag_name = $1 AND guildId = $2", tag, str(guildId))		
		
		if not checkTag:
			embed = discord.Embed(
				color = discord.Color.random(),
				description="> No tag found with that name!"
			)
			await ctx.respond(embed=embed)
		else:	
			await self.bot.pg_con.fetchval(
				"DELETE FROM tags WHERE tag_name = $1", 
				tag
			)
			embed = discord.Embed(
				color = discord.Color.random(),
				description="> Suceesfully deleted"
			)
			await ctx.respond(embed=embed)

				
def setup(bot):
	bot.add_cog(slashTags(bot))