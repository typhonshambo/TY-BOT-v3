import discord
from discord.ext import commands
from discord.commands import Option, slash_command
import json

with open ('././config/guilds.json', 'r') as f:
	data = json.load(f)
	guilds = data['guilds']


class memberinfo(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(
		description="sends latency of BOT",
		guild_ids=guilds
	)
	async def userinfo(self, ctx, member: Option(discord.Member, "Mention a user",required=False, default=None)):
		
		
		
		if not member:
			member = ctx.author
		userAvatar = member.avatar.url
		embed = discord.Embed(title="User Information", color=ctx.author.color)
		embed.set_thumbnail(url=userAvatar)

		fields = [("Name", str(member), True), ("ID", member.id, True), ("Top Role", member.top_role.mention, True), ("Account Created (UTC)", member.created_at.strftime("%m/%d/%Y %H:%M:%S"), True), ("Account Joined (UTC)", member.joined_at.strftime("%m/%d/%Y %H:%M:%S"), True), ("Boosted", bool(member.premium_since), True)]

		for name, value, inline in fields:
			embed.add_field(name=name, value=value, inline=inline)

		embed.set_footer(text="Command Requested By {}".format(ctx.author.name), icon_url=ctx.author.avatar.url)
		await ctx.respond(embed=embed)

def setup(bot):
	bot.add_cog(memberinfo(bot))