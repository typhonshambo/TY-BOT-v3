import discord
from discord import Webhook
from discord.ext import commands
import json
import aiohttp
import os

webhookUrl = os.environ.get['welcomeWebhookUrl']


class welcomer(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.Cog.listener() 
	async def on_member_join(self, member):
		
		embed = discord.Embed(
			title = """━━━━━━━━━━━━━━━━━━
			""",
			
			color = discord.Color.red()
		)
		#embed.set_thumbnail(url = "https://media.discordapp.net/attachments/763456369683726336/799333265328701510/miniGif_20210114231432.gif")
		embed.set_image(url = "https://cdn.discordapp.com/attachments/763456369683726336/805534583701241866/ezgif-1-7233f8e32747.gif")
		embed.set_thumbnail(url=member.display_avatar.url)
		embed.add_field(name = f"Welcome {member.name}", value =f"""\u200b
		:negative_squared_cross_mark: Your position  -->  {member.guild.member_count}
		:negative_squared_cross_mark:  User ID       -->  {member.mention}
		
		\u200b━━━━━━━━━━━━━━━━━━━━━
		:diamonds: <#814735113781903360> : Our server tour
		:diamonds: <#615038940428107778> : Some of simple rules
		:diamonds: <#814550586656555038> : Chat here !
		━━━━━━━━━━━━━━━━━━━━━
		""" , inline = True)
		 
		async def foo():
			async with aiohttp.ClientSession() as session:
				webhook = Webhook.from_url(webhookUrl, session=session)
				await webhook.send(embed=embed, username='Welcome', avatar_url="https://media.discordapp.net/attachments/869155012809474068/959039088927838228/unknown.png?width=326&height=326")
		await foo()

def setup(bot):
	bot.add_cog(welcomer(bot))