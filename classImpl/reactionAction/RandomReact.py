import discord
from reactionAction.AbstractReactionAction import _reactionAction
import random

class RandomReact(_reactionAction):

    async def _technique(self,reaction):
        await reaction.message.add_reaction(discord.PartialEmoji(name=random.choice(self.emoji_list)))

