import discord
from discord.ext import commands
from discord.commands import CommandPermission, SlashCommandGroup
import json

with open ('././config/guilds.json', 'r') as f:
	data = json.load(f)
	guilds = data['guilds']

with open ('././config/guilds.json', 'r') as f:
	data = json.load(f)
	modeRole = data['modRole']
	muteRole = data['mutedRole']

	
class slashMute(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	mute = SlashCommandGroup(
		"mute",
		"Mute/unmute a member",
		permissions=[CommandPermission(int(modeRole), 1, True)],
		guild_ids=guilds
	)
	
	@mute.command(description="🔇Mute a member")
	async def user(self, ctx,member: discord.Member):
		await ctx.response.defer()
		mute_ = ctx.guild.get_role(int(muteRole))
		await member.edit(roles=[mute_])
		
		embed = discord.Embed(
			color = discord.Color.random(),
			description = f"> {member.mention}has been muted!"
		)
		await ctx.respond(embed=embed)

	@mute.command(description="🔊Unmute a member")
	async def unmute(self, ctx,member: discord.Member):
		await ctx.response.defer()
		await member.edit(roles=[])
		
		embed = discord.Embed(
			color = discord.Color.random(),
			description = f"> {member.mention}has been Unmuted!"
		)
		await ctx.respond(embed=embed)

def setup(bot):
	bot.add_cog(slashMute(bot))