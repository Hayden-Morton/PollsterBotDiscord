import discord
from reactionAction.AbstractReactionAction import _reactionAction

class UpToInclusive(_reactionAction):

    async def _technique(self,reaction):
        await reaction.clear()

        for i in range(self.emoji_list.index(reaction.emoji)+1):
            await reaction.message.add_reaction(discord.PartialEmoji(name=self.emoji_list[i]))
