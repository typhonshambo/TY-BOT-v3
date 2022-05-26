import discord
from discord.ext import commands
from discord import Embed, Webhook
import DiscordUtils 
import aiohttp
import os

webhookUrl = os.environ.get('inviteLogWebhookUrl')

class inviteLog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.tracker = DiscordUtils.InviteTracker(bot)
		

	@commands.Cog.listener() 
	async def on_member_join(self, member):

		inviter = await self.tracker.fetch_inviter(member)
		embed = discord.Embed(
			color = discord.Color.random(),
			timestamp=discord.utils.utcnow(),
			description = f"""
			> {inviter} invited {member.mention}
			"""
		)
		embed.set_thumbnail(url=member.display_avatar.url)

		async def foo():
			async with aiohttp.ClientSession() as session:
				webhook = Webhook.from_url(webhookUrl, session=session)
				await webhook.send(embed=embed, username='invites', avatar_url="https://media.discordapp.net/attachments/869155012809474068/959039088927838228/unknown.png?width=326&height=326")
		await foo()


def setup(bot):
	bot.add_cog(inviteLog(bot))