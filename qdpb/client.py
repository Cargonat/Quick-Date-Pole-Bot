import discord
from qdpb import processor


# override discord client class to add own functionality
class QDPBClient(discord.Client):
    def __init__(self, **options):
        super().__init__(**options)
        self.processor = processor.Processor()

    # override
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    # override
    # called whenever a new message arrives
    async def on_message(self, message):
        # don' process own messages
        if message.author == self.user:
            return
        # don't process messages without keyword
        if message.content.find("/datepoll") == -1:
            return
        self.processor.process_message(message)
