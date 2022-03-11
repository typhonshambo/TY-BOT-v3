import discord
from discord.ext import commands
from discord.commands import Option, slash_command, SlashCommandGroup
from discord.ext.commands import has_permissions, MissingPermissions, MissingRequiredArgument
import json

with open ('././config/guilds.json', 'r') as f:
	data = json.load(f)
	guilds = data['guilds']

class slashKick(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
 
	@commands.slash_command(
		description="kick a member",
		guild_ids=guilds
	)
	@commands.has_permissions(administrator=True)
	async def kick(
		self, 
		ctx, 
		member: Option(discord.Member, "Mention a user",required=False),
		reason: Option(str, "Provide reason", required=False)
		):
		await ctx.response.defer()
		if member == ctx.author:
				embed=discord.Embed(
					description = f'❌You cannot kick yourself!',
					color=0xFC0255
				)
				await ctx.respond(embed=embed)
		
		else:
			embed = discord.Embed(
				description = f'You have `Kicked` from: `{ctx.guild.name}` **Reason**:`{reason}`', 
				color = discord.Color.red(),
				timestamp=discord.utils.utcnow()
			)
			await member.send(embed=embed)

			
			embed_mod = discord.Embed(
				description =f"`{member.display_name}` has been kicked\n`Reason` : {reason}",
				color = discord.Color.red(),
				timestamp=discord.utils.utcnow()
			)
			await ctx.respond(embed=embed_mod)
			await member.kick(reason=reason)

	@kick.error
	async def kick_error(self, ctx, error):
		if isinstance(error, MissingPermissions):

			text = discord.Embed(
				description = f'Sorry `{ctx.author}`, you do not have permissions to do that!',
				color = discord.Color.blue()
			)
			await ctx.respond(embed=text)
			

def setup(bot):
	bot.add_cog(slashKick(bot))