import discord
from reactionAction.AbstractReactionAction import _reactionAction

class AddFill(_reactionAction):

    async def _technique(self,reaction):

        for emoji in self.emoji_list:
            await reaction.message.add_reaction(discord.PartialEmoji(name=emoji))
