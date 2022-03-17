from email.policy import default
import discord
from discord.ext import commands
from discord.commands import Option, slash_command, SlashCommandGroup
from discord import File
from easy_pil import Editor, load_image_async, Font, Canvas
import json
import urllib.request

with open ('././config/guilds.json', 'r') as f:
	data = json.load(f)
	guilds = data['guilds']

def imgDownloader(link):
	resource = urllib.request.urlopen(link)
	output = open("././assets/levelBG2.png","wb")
	output.write(resource.read())
	output.close()



class slashLevel(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	levelCmd = SlashCommandGroup("level", "Check Your level", guild_ids=guilds)

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author == self.bot.user:
			return

		author_id = str(message.author.id)
		guild_id = str(message.guild.id)
		default_background = "https://raw.githubusercontent.com/typhonshambo/TY-BOT-v3/main/assets/levelBG1.png"
		default_color = "#E9DAC7"
		user = await self.bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1 AND guild_id = $2", author_id, guild_id)
		
		if not user:
			await self.bot.pg_con.execute("INSERT INTO users (user_id, guild_id , lvl, xp, background, color) VALUES ($1, $2, 1, 0, $3, $4)", author_id, guild_id, default_background, default_color)
		
		#user = await self.bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1 AND guild_id = $2", author_id, guild_id)
		await self.bot.pg_con.execute("UPDATE users SET xp = $1 WHERE user_id = $2 AND guild_id = $3", user['xp'] + 1, author_id, guild_id)

		cur_xp = user['xp']
		cur_lvl = user['lvl']

		if cur_xp >= round((4 * (cur_lvl ** 3))/5):
			await self.bot.pg_con.execute("UPDATE users SET lvl = $1 WHERE user_id = $2 AND guild_id = $3",user['lvl'] + 1, user['user_id'], user['guild_id'])
		   # await message.channel.send(f"`{message.author.display_name}` is now at level {user['lvl'] + 1}")

	@levelCmd.command(
			description="Check Your level",
			guild_ids=guilds
	)
	async def check(
		self, 
		ctx, 
		member: Option(discord.Member, "Mention a user",required=False)
	):
		await ctx.response.defer()
		
		try:
			member = ctx.author if not member else member
			member_id = str(member.id)
			guild_id = str(ctx.guild.id)
			user = await self.bot.pg_con.fetch("SELECT * FROM users WHERE user_id = $1 AND guild_id = $2", member_id, guild_id)
			if not user:
				embed = discord.Embed(
					color = discord.Color.random(),
					description= "> Member doesn't have any level, please send some messages"
				)
				await ctx.respond(embed=embed)

			imgDownloader(user[0]["background"])

			if member != None: 
				percentage = ((user[0]['xp'])/(round((4 * ((user[0]['lvl']) ** 3))/5))) * 100
					
				background = Editor("././assets/levelBG2.png")
				profile = await load_image_async(str(member.avatar.url))

				profile = Editor(profile).resize((150, 150)).circle_image()

				poppins = Font().poppins(size=40)
				poppins_small = Font().poppins(size=30)

				square = Canvas((500, 500), str(user[0]["color"]))
				square = Editor(square)
				square.rotate(30, expand=True)

				background.paste(square.image, (600, -250))
				background.paste(profile.image, (30, 30))

				background.rectangle((30, 220), width=650, height=40, fill="white", radius=20)
				background.bar((30, 220), max_width=650, height=40, percentage=percentage ,fill="#FF56B2", radius=20)
				background.text((200, 40), str(member), font=poppins, color="white")

				background.rectangle((200, 100), width=350, height=2, fill="#17F3F6")
				background.text((200, 130), f"Level : {user[0]['lvl']}" + f" XP : {user[0]['xp']}", font=poppins_small, color="white")

				file = File(fp=background.image_bytes, filename="card.png")
				await ctx.respond(file=file)
			
			if member == None:
					percentage = ((user[0]['xp'])/(round((4 * ((user[0]['lvl']) ** 3))/5))) * 100
					
					background = Editor("././assets/levelBG2.png")
					profile = await load_image_async(str(ctx.author.avatar_url))

					profile = Editor(profile).resize((150, 150)).circle_image()

					poppins = Font().poppins(size=40)
					poppins_small = Font().poppins(size=30)

					square = Canvas((500, 500), str(user[0]["color"]))
					square = Editor(square)
					square.rotate(30, expand=True)

					background.paste(square.image, (600, -250))
					background.paste(profile.image, (30, 30))

					background.rectangle((30, 220), width=650, height=40, fill="white", radius=20)
					background.bar((30, 220), max_width=650, height=40, percentage=percentage ,fill="#FF56B2", radius=20)
					background.text((200, 40), str(ctx.author), font=poppins, color="white")

					background.rectangle((200, 100), width=350, height=2, fill="#17F3F6")
					background.text((200, 130), f"Level : {user[0]['lvl']}" + f" XP : {user[0]['xp']}", font=poppins_small, color="white")

					file = File(fp=background.image_bytes, filename="card.png")
					await ctx.respond(file=file)
		except:
			embed = discord.Embed(
				color = discord.Color.random(),
				description="> Some error occurred!\nMaybe sending some messages may work!"
			)	
			await ctx.respond(embed=embed)
	

	@levelCmd.command(
		description="Customize your level card",
		guild_ids=guilds
	)
	async def set(
		self, 
		ctx,
		background: Option(str, "enter level background link", default="https://raw.githubusercontent.com/typhonshambo/TY-BOT-v3/main/assets/levelBG1.png"),
		canvas: Option(str, "Enter Canvas Color", default="#E9DAC7")
	):
	
		member_id = str(ctx.author.id)
		guild_id = str(ctx.guild.id)
		await ctx.response.defer()

		await self.bot.pg_con.execute("UPDATE users SET background = $1, color = $2 WHERE user_id = $3 AND guild_id = $4",background, str(canvas) ,member_id, guild_id)
		embed = discord.Embed(
			color = discord.Color.random(),
			description="> Done!"
		)
		await ctx.respond(embed=embed)
		
def setup(bot):
	bot.add_cog(slashLevel(bot))