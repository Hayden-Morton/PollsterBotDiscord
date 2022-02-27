import discord
from reactionAction.AbstractReactionAction import _reactionAction

class RemoveAll(_reactionAction):

    async def _technique(self,reaction):
        await reaction.message.clear_reactions()
