from reactionAction.AbstractReactionAction import _reactionAction
import discord

class BetweenInclusive(_reactionAction):

    async def _technique(self,reaction):
        for other_reaction in reaction.message.reactions:
            if (other_reaction != reaction) and (other_reaction.emoji in self.emoji_list):
                start_index = self.emoji_list.index(other_reaction.emoji)
                end_index = self.emoji_list.index(reaction.emoji)
                
                await reaction.clear() 
                await other_reaction.clear() 

                index = start_index
                while True: #repeat until
                    await reaction.message.add_reaction(discord.PartialEmoji(name=self.emoji_list[index]))

                    if index == end_index:
                        break

                    index += 1
                    if index > len(self.emoji_list) - 1:
                        index = 0
                
                return
