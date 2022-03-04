import discord
import botRef

from reactionAction import *

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        emoji_numbers = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟'] #glitched formatting in text
        emoji_day_letters = ['🇲','🇹','🇼','🇭','🇫','🇸','🇺']
        emoji_thumbs = ['👍','👎','🤷']
        emoji_easter_egg = ['🥚','🐰']
        emoji_reset = ['🔄']
        emoji_PSR = ['🧻','✂️','🪨']

        self.preReactionActions = []

        #self.preReactionActions.append(RemoveAll.RemoveAll(emoji_reset))

        self.postReactionActions = []
        self.postReactionActions.append(UpToInclusive.UpToInclusive(emoji_numbers))
        self.postReactionActions.append(BetweenInclusive.BetweenInclusive(emoji_day_letters))
        self.postReactionActions.append(MentionThumbs.MentionThumbs(emoji_thumbs))
        self.postReactionActions.append(AddFill.AddFill(emoji_easter_egg))
        self.postReactionActions.append(RandomReact.RandomReact(emoji_PSR))

        intents = discord.Intents(members=True,guilds=True)
    

    async def on_ready(self):
        print('We have logged in as {0}'.format(self.user.name))

    async def on_reaction_add(self, reaction, user):
            
        if (user == self.user):
            return
        
        for action in self.preReactionActions:
            await action.run(reaction)

        for react in reaction.message.reactions:
            if react.me:
                return

        for action in self.postReactionActions:
            await action.run(reaction)

MyClient().run(botRef.token)

