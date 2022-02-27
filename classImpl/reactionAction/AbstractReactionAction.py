class _reactionAction(object):

    def __init__(self,emoji_list):
        self.emoji_list = emoji_list

    async def run(self,reaction):
        if reaction.emoji in self.emoji_list:
            await self._technique(reaction)

    async def _technique(self,reaction):
        pass
