import discord
import re
from piazza_api import Piazza
import config


class Client(discord.Client):
    def __init__(self):
        super(Client, self).__init__()

        # Regex to check if message wants a post
        self.re = re.compile("p([0-9])+", re.IGNORECASE)

        # Piazza setup
        p = Piazza()
        p.user_login()
        self.network = p.network("kmfs2bmdr9syz") # CSE 13S

    async def on_ready(self):
        print("Connected as {}".format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        match = self.re.search(message.content)
        if match:
            post = match.group()[1:]
            await message.reply("https://piazza.com/class/kmfs2bmdr9syz?cid={}".format(post, post))

def main():
    client = Client()
    client.run(config.token)

if __name__ == "__main__":
    main()
