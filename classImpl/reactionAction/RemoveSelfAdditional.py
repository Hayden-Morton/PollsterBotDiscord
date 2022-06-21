import discord
from reactionAction.AbstractReactionAction import _reactionAction

class RemoveSelfAdditional(_reactionAction):

    async def _technique(self,reaction):
        for other_reaction in reaction.message.reactions:
            users = await other_reaction.users().flatten()
            if len(users) > 1:
                for user in users:
                    if user.bot:
                        await other_reaction.remove(user)
        
        await reaction.clear()
