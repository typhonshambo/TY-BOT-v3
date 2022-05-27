import discord
from discord import Webhook
from discord.ext import commands
import json
import aiohttp



with open ('././config/webhooks.json', 'r') as f:
	data = json.load(f)
	webhookUrl = data['modmail']

class modmail(commands.Cog):
	def __init__ (self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.id == self.bot.user.id:
			return
		#Checks if the DM'er is a bot or no,
		if message.author != message.author.bot:
			if not message.guild: #Checks if the message is in a Guild or no.
				embed = discord.Embed(description='> Support will be with you Shortly.', color = discord.Color.green(), timestamp = message.created_at)
				embed.set_footer(text ="Please use links to transfer Images & Files.")
				await message.author.send(embed = embed)

				embed2 = discord.Embed(color = discord.Color.orange(), timestamp = message.created_at)
				embed2.add_field(name = "Message from {}".format(message.author), value = f"{message.content}")

				async def foo():
					async with aiohttp.ClientSession() as session:
						webhook = Webhook.from_url(webhookUrl, session=session)
						await webhook.send(embed=embed2, username='Modmail', avatar_url="https://media.discordapp.net/attachments/869155012809474068/959039088927838228/unknown.png?width=326&height=326")
				await foo()

def setup(bot):
	bot.add_cog(modmail(bot))
