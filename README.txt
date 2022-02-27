Program Name: Pollster Bot
Author: Hayden Morton
Date: 22/02/2022

Purpose: Allow for easier Polls in discord using reactions

	Bot is run locally on author's machine

	Only works for new messages sent while bot is active.

Run:
	python3 classImpl/main.py


SetUp:
	copy this link into webpage, and add the bot to the desired server.
	https://discord.com/api/oauth2/authorize?client_id=945259261074747403&permissions=9280&scope=bot


Use (in discord Client in server bot is added to):


	Poll of Numbered Options:
		react the number of options:
			bot will remove and fill with the options up to 10
		

	Poll of Day Letters:
		react the range of days letters (M T W H F S U):
			bot will remove both and fill in order

	
	Mention Thumbs:	
		react to a message containing a mention of a role with (thumbs Up, Down, Shrug):
			bot will add the missing

	Clear all Reactions:
		react with counter_clockwise_arrows:
			bot will remove all reactions



Developer Links:
https://discord.com/developers/applications/945259261074747403/bot

