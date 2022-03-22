import discord
from discord.ext import commands
from discord.commands import Option, slash_command, SlashCommandGroup
import json
import random
from typing import List

with open ('././config/guilds.json', 'r') as f:
	data = json.load(f)
	guilds = data['guilds']

class TicTacToeButton(discord.ui.Button["TicTacToe"]):
	def __init__(self, x: int, y: int):
		super().__init__(style=discord.ButtonStyle.secondary, label="\u200b", row=y)
		self.x = x
		self.y = y

	async def callback(self, interaction: discord.Interaction):
		assert self.view is not None
		view: TicTacToe = self.view
		state = view.board[self.y][self.x]
		if state in (view.X, view.O):
			return

		if interaction.user != view.player1 and interaction.user != view.player2:
			return await interaction.response.send_message(embed=discord.Embed(description="**<:error:897382665781669908> This isn't your game!**", color=discord.Color.red()), ephemeral=True)

		elif interaction.user == view.player1 and view.current_player == view.O:
			return await interaction.response.send_message(embed=discord.Embed(description="**<:error:897382665781669908> It isn't your turn!**", color=discord.Color.red()), ephemeral=True)

		elif interaction.user == view.player2 and view.current_player == view.X:
			return await interaction.response.send_message(embed=discord.Embed(description="**<:error:897382665781669908> It isn't your turn!**", color=discord.Color.red()), ephemeral=True)

		if view.current_player == view.X:
			self.emoji = "<:ttt_x:930542490862379130>"
			self.disabled = True
			view.board[self.y][self.x] = view.X
			view.current_player = view.O
			content = f"It is now {view.player2.mention}'s turn (O)"
		else:
			self.emoji = "<:ttt_o:930542761638244483>"
			self.disabled = True
			view.board[self.y][self.x] = view.O
			view.current_player = view.X
			content = f"It is now {view.player1.mention}'s turn (X)"

		winner = view.check_board_winner()
		if winner is not None:
			if winner == view.X:
				content = f"{view.player1.mention} won!"
				view.ended = True
			elif winner == view.O:
				content = f"{view.player2.mention} won!"
				view.ended = True
			else:
				content = "It's a tie!"
				view.ended = True

			for child in view.children:
				child.disabled = True

			view.stop()

		await interaction.response.edit_message(content=content, view=view)



class TicTacToe(discord.ui.View):
	children: List[TicTacToeButton]
	X = -1
	O = 1

	def __init__(self, player1: discord.Member, player2: discord.Member, message: discord.Message):
		super().__init__(timeout=80)
		self.Tie = -2
		self.current_player = self.X
		self.player1 =  player1
		self.player2 = player2
		self.ended = False
		self.message = message
		self.board = [
			[0, 0, 0],
			[0, 0, 0],
			[0, 0, 0],
		]

		for x in range(3):
			for y in range(3):
				self.add_item(TicTacToeButton(x, y))

	def check_board_winner(self):
		for across in self.board:
			value = sum(across)
			if value == 3:
				return self.O
			elif value == -3:
				return self.X

		for line in range(3):
			value = self.board[0][line] + self.board[1][line] + self.board[2][line]
			if value == 3:
				return self.O
			elif value == -3:
				return self.X

		diag = self.board[0][2] + self.board[1][1] + self.board[2][0]
		if diag == 3:
			return self.O
		elif diag == -3:
			return self.X

		diag = self.board[0][0] + self.board[1][1] + self.board[2][2]
		if diag == 3:
			return self.O
		elif diag == -3:
			return self.X

		if all(i != 0 for row in self.board for i in row):
			return self.Tie

		return None

	async def on_timeout(self):
		if self.ended == True:
			return
		for child in self.children:
			child.disabled = True
		
		return await self.message.edit(content=None, embed=discord.Embed(description="**<:error:897382665781669908> The game ended | Player(s) didn't respond within time!**", color=discord.Color.red()), view=self)

class slashFun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.slash_command(guild_ids=guilds,description="Play a TicTacToe Game with Someone Online!")
	async def tictactoe(self, ctx: discord.ApplicationContext, user: Option(discord.Member, "The user you want to play tic-tac-toe with", default=None, required=True)):
		if user is None:
			return await ctx.respond(embed=discord.Embed(description="**You can't play tic-tac-toe alone!**", color=discord.Color.red()), ephemeral=True)

		if user.bot:
			return await ctx.respond(embed=discord.Embed(description="**You can't play with a bot!**", color=discord.Color.red()), ephemeral=True)

		players = {
			str(ctx.author.id): str(user.id),
			str(user.id): str(ctx.author.id)
		}

		player1 = random.choice(list(players.keys()))
		player2 = players[player1]

		await ctx.interaction.response.send_message(f"{ctx.guild.get_member(int(player1)).mention}\'s turn (X)")
		
		msg = await ctx.interaction.original_message()

		await msg.edit(view=TicTacToe(
			player1=ctx.guild.get_member(int(player1)),
			player2=ctx.guild.get_member(int(player2)),
			message=msg
		))

def setup(bot):
	bot.add_cog(slashFun(bot))