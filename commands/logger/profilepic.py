import discord
from discord import Webhook
from discord.ext import commands
import json
import aiohttp



with open ('././config/webhooks.json', 'r') as f:
	data = json.load(f)
	webhookUrl = data['avatar']


	

class pfplogger(commands.Cog):
	def __init__(self, bot): 
		self.bot = bot



	@commands.Cog.listener()
	async def on_user_update(self, before, after):
	
		if before.name != after.name:
				embed = discord.Embed(title="Upgrade Name",
								colour=after.colour,
								timestamp=discord.utils.utcnow())

				fields = [("Before", before.name, False),
							("After", after.name, False)]

				for name, value, inline in fields:
					embed.add_field(name=name, value=value, inline=inline)

				async def foo():
					async with aiohttp.ClientSession() as session:
						webhook = Webhook.from_url(webhookUrl, session=session)
						await webhook.send(embed=embed, username='PFP LOG', avatar_url="https://media.discordapp.net/attachments/869155012809474068/959039088927838228/unknown.png?width=326&height=326")
				await foo()

		if before.name != after.name:
				embed = discord.Embed(title="Upgrade Tag",
								colour=after.colour,
								timestamp=discord.utils.utcnow())

				fields = [("After", before.discriminator, False),
							("Before", after.discriminator, False)]

				for name, value, inline in fields:
					embed.add_field(name=name, value=value, inline=inline)
				
				async def foo():
					async with aiohttp.ClientSession() as session:
						webhook = Webhook.from_url(webhookUrl, session=session)
						await webhook.send(embed=embed, username='PFP LOG', avatar_url="https://media.discordapp.net/attachments/869155012809474068/959039088927838228/unknown.png?width=326&height=326")
				await foo()

		if before.avatar.url != after.avatar.url:
				embed = discord.Embed(title="Upgrade Avatar",
								description=f"""`{before.display_name}` avatar changed 
								(the old one on the right):arrow_forward: 
								(The image below is the new one):arrow_down_small: 
								""",
								colour= discord.Color.blurple(),
								timestamp=discord.utils.utcnow())

				embed.set_thumbnail(url=before.avatar.url)
				embed.set_image(url=after.avatar.url)

				async def foo():
					async with aiohttp.ClientSession() as session:
						webhook = Webhook.from_url(webhookUrl, session=session)
						await webhook.send(embed=embed, username='PFP LOG', avatar_url="https://media.discordapp.net/attachments/869155012809474068/959039088927838228/unknown.png?width=326&height=326")
				await foo()



def setup(bot):
	bot.add_cog(pfplogger(bot))