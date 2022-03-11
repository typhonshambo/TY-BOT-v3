import discord
from discord.ext import commands
from discord.commands import Option, slash_command, SlashCommandGroup
from discord import File
from easy_pil import Editor, load_image_async, Font, Canvas
import json

with open ('././config/guilds.json', 'r') as f:
	data = json.load(f)
	guilds = data['guilds']

class slashLevel(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author == self.bot.user:
			return

		author_id = str(message.author.id)
		guild_id = str(message.guild.id)

		user = await self.bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1 AND guild_id = $2", author_id, guild_id)
		
		if not user:
			await self.bot.pg_con.execute("INSERT INTO users (user_id, guild_id , lvl, xp) VALUES ($1, $2, 1, 0)", author_id, guild_id)
		
		#user = await self.bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1 AND guild_id = $2", author_id, guild_id)
		await self.bot.pg_con.execute("UPDATE users SET xp = $1 WHERE user_id = $2 AND guild_id = $3", user['xp'] + 1, author_id, guild_id)

		cur_xp = user['xp']
		cur_lvl = user['lvl']

		if cur_xp >= round((4 * (cur_lvl ** 3))/5):
			await self.bot.pg_con.execute("UPDATE users SET lvl = $1 WHERE user_id = $2 AND guild_id = $3",user['lvl'] + 1, user['user_id'], user['guild_id'])
		   # await message.channel.send(f"`{message.author.display_name}` is now at level {user['lvl'] + 1}")

	@commands.slash_command(
			description="Check Your level",
			guild_ids=guilds
	)
	async def level(
		self, 
		ctx, 
		member: Option(discord.Member, "Mention a user",required=False)
	):
		await ctx.response.defer()
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

		if member != None: 
			percentage = ((user[0]['xp'])/(round((4 * ((user[0]['lvl']) ** 3))/5))) * 100
				
			background = Editor("././assets/levelBG1.png")
			profile = await load_image_async(str(member.avatar.url))

			profile = Editor(profile).resize((150, 150)).circle_image()

			poppins = Font().poppins(size=40)
			poppins_small = Font().poppins(size=30)

			square = Canvas((500, 500), "#E9DAC7")
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
				
				background = Editor("././assets/levelBG1.png")
				profile = await load_image_async(str(ctx.author.avatar_url))

				profile = Editor(profile).resize((150, 150)).circle_image()

				poppins = Font().poppins(size=40)
				poppins_small = Font().poppins(size=30)

				square = Canvas((500, 500), "#E9DAC7")
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
			
def setup(bot):
	bot.add_cog(slashLevel(bot))