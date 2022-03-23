import discord
from discord.ext import commands
from discord.commands import Option, slash_command
import json


with open ('././config/guilds.json', 'r') as f:
	data = json.load(f)
	guilds = data['guilds']

	
class NitroView(discord.ui.View):
	def __init__(self, msg: discord.Message, ctx: commands.Context):
		super().__init__(timeout=30)
		self.msg = msg
		self.ctx = ctx

	@discord.ui.button(label="Claim", style=discord.ButtonStyle.success, emoji="<:nitro:914110236707680286>")
	async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
		if interaction.user != self.ctx.author:
			embed = discord.Embed(description=f"<:error:897382665781669908> You can't do that {interaction.user.mention}!", color=discord.Color.red())
			return await self.ctx.send(embed=embed, delete_after=5)
		button.label = "Claimed"
		button.style = discord.ButtonStyle.danger
		button.emoji = "<:nitro:914110236707680286>"
		button.disabled = True
		await interaction.response.send_message(content="https://imgur.com/NQinKJB", ephemeral=True)
		embed = discord.Embed(description=f"***<:nitro:914110236707680286> {self.ctx.author.mention} claimed the nitro!***", color=discord.Color.nitro_pink())
		embed.set_image(url="https://media.discordapp.net/attachments/886639021772648469/903535585992523796/unknown.png")
		await self.msg.edit(embed=embed, view=self)

	async def on_timeout(self):
		for child in self.children:
			if child.disabled:
				return
		for child in self.children:
			child.disabled = True
		embed = discord.Embed(description=f"**<:error:897382665781669908> Looks like either {self.ctx.author.mention} didn't wanna have it or {self.ctx.author.mention} went AFK**", color=discord.Color.red())
		embed.set_image(url="https://media.discordapp.net/attachments/886639021772648469/903535585992523796/unknown.png")
		await self.msg.edit(embed=embed, view=self)


class slashNitro(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@slash_command(description="Generates a nitro link!", guild_ids=guilds)
	async def nitro(self, ctx):
		interaction: discord.Inteaction = ctx.interaction
		embed = discord.Embed(description=f"**{ctx.author.mention} generated a nitro link!**", color=discord.Color.nitro_pink())
		embed.set_image(url="https://media.discordapp.net/attachments/886639021772648469/903535585992523796/unknown.png")
		await interaction.response.send_message(embed=embed)
		message = await interaction.original_message()
		await message.edit(embed=embed, view=NitroView(message, ctx))

		
def setup(bot):
	bot.add_cog(slashNitro(bot))