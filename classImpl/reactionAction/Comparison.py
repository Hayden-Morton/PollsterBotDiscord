import discord
from reactionAction.AbstractReactionAction import _reactionAction

class Comparison(_reactionAction):

    def __init__(self, emoji_list,response_list):
        super().__init__(emoji_list)
        self.emoji_failure_response = response_list[0]
        self.emoji_success_response = response_list[1]

    async def _technique(self,reaction):
        for other_reaction in reaction.message.reactions:
            if (other_reaction != reaction) and (other_reaction.emoji in self.emoji_list):
                if (reaction.emoji == other_reaction.emoji):
                    await reaction.message.clear_reactions()
                if (self.emoji_list.index(reaction.emoji) > self.emoji_list.index(other_reaction.emoji)) or (self.emoji_list.index(reaction.emoji) == 0 and self.emoji_list.index(other_reaction.emoji) == (len(self.emoji_list) -1)): 
                    for response in self.emoji_success_response:
                        await reaction.message.add_reaction(discord.PartialEmoji(name = response)) 
                else: 
                     for response in self.emoji_failure_response:
                        await reaction.message.add_reaction(discord.PartialEmoji(name = response)) 
                    
                
                return
