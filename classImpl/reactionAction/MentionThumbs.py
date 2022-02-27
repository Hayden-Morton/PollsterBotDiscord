import discord
from reactionAction.AddFill import AddFill

class MentionThumbs(AddFill):

    async def _technique(self,reaction):
        if len(reaction.message.role_mentions) > 0:
            await super()._technique(reaction)

