import discord
from discord.ext import commands
from discord.commands import Option, slash_command, SlashCommandGroup
from discord.ext.commands import has_permissions, MissingPermissions, MissingRequiredArgument
import json

with open ('././config/guilds.json', 'r') as f:
	data = json.load(f)
	guilds = data['guilds']

class slashBan(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
 
	@commands.slash_command(
		description="ban a member",
		guild_ids=guilds
	)
	@commands.has_permissions(administrator=True)
	async def ban(
		self, 
		ctx, 
		member: Option(discord.Member, "Mention a user",required=True, default=None),
		reason: Option(str, "Provide reason", required=False)
		):
		await ctx.response.defer()
		if member == ctx.author:
				embed=discord.Embed(
					description = f'❌You cannot ban yourself!',
					color=0xFC0255
				)
				await ctx.respond(embed=embed)
		
		else:
			embed = discord.Embed(
				description = f'You have `Banned` from: `{ctx.guild.name}` **Reason**:`{reason}`', 
				color = discord.Color.red(),
				timestamp=discord.utils.utcnow()
			)
			await member.send(embed=embed)

			
			embed_mod = discord.Embed(
				description =f"`{member.display_name}` has been Banned\n`Reason` : {reason}",
				color = discord.Color.red(),
				timestamp=discord.utils.utcnow()
			)
			await ctx.respond(embed=embed_mod)
			await ctx.guild.ban(member, reason=reason)

	@ban.error
	async def ban_error(self, ctx, error):
		if isinstance(error, MissingPermissions):

			text = discord.Embed(
				description = f'Sorry `{ctx.author}`, you do not have permissions to do that!',
				color = discord.Color.blue()
			)
			await ctx.respond(embed=text)
			
	@commands.slash_command(
		description="Unban a member",
		guild_ids=guilds
	)
	@commands.has_permissions(administrator=True)
	async def unban(
		self, 
		ctx, 
		member: Option(discord.Member, "Mention a user",required=True, default=None),
		):
			await ctx.response.defer()
			banned_users = await ctx.guild.bans()
			for ban_entry in banned_users:
				user = ban_entry.user

				if (user.id) == (member):
					await ctx.guild.unban(user)
					unban_msg=discord.Embed(
						description=f"{user.mention} is unbanned!",
						color=0xA902FC,
						timestamp=discord.utils.utcnow()
					)
					await ctx.respond(embed=unban_msg)
				else:
					msg=discord.Embed(
						description=f"`{member}` is already unbanned!",
						color=0xA902FC,
						timestamp=discord.utils.utcnow()
					)
					await ctx.respond(embed=msg)	
	@unban.error
	async def unban_error(self, ctx, error):
		if isinstance(error, MissingPermissions):

			text = discord.Embed(
				description = f'Sorry `{ctx.author}`, you do not have permissions to do that!',
				color = discord.Color.blue()
			)
			await ctx.respond(embed=text)
def setup(bot):
	bot.add_cog(slashBan(bot))