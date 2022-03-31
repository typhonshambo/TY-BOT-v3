import discord
from discord.ext import commands

class database(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_ready(self):
		print("[\] setting up DATABASE")
		
		#for leveling
		await self.bot.pg_con.execute("""
		CREATE TABLE IF NOT EXISTS users
		(
			guild_id character varying,
			lvl integer,
			user_id character varying NOT NULL,
			xp integer,
			background character varying,
			color character varying
		);
		""")
		print("[\] DATABASE READY")

		
	@commands.Cog.listener() 
	async def on_member_join(self, member):
		background= "https://raw.githubusercontent.com/typhonshambo/TY-BOT-v3/main/assets/levelBG1.png"
		canvas = "#E9DAC7"
		member_id = str(member.id)
		guild_id = str(member.id) 
		await self.bot.pg_con.execute("UPDATE users SET background = $1, color = $2 WHERE user_id = $3 AND guild_id = $4",background, str(canvas) ,member_id, guild_id)

		
def setup(bot):
	bot.add_cog(database(bot))