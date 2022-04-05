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
			xp integer
		);
		""")
		print("[\] DATABASE READY")

		

		
def setup(bot):
	bot.add_cog(database(bot))