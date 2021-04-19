import discord
import re
import config


class Client(discord.Client):
    def __init__(self):
        super(Client, self).__init__()

        # Regex to check if message wants a post
        self.re = re.compile(r"(^|\s)p([0-9]+)", re.IGNORECASE)

    async def on_ready(self):
        print("Connected as {}".format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        match = self.re.search(message.content)
        if match:
            post = match.group(2)
            reply = await message.reply(("Piazza @{}: https://piazza.com/class/kmfs2bmdr9syz?cid={}\n"
                    "(<@{}> can delete by reacting)").format(post, post, message.author.id))
            await reply.add_reaction("🗑️")

    async def on_raw_reaction_add(self, payload):
        if payload.user_id == self.user.id:
            # ignore our own reactions
            return

        # only wastebasket emoji reactions since that's what the bot reacts with
        if payload.emoji.name == "🗑️":
            channel = self.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            # is it our message?
            if message.author == self.user:
                # is the reaction from the user who sent the original message?
                # check by seeing if they're mentioned as the bot mentions the user who sent it
                if payload.user_id in [user.id for user in message.mentions]:
                    await message.delete()

def main():
    client = Client()
    client.run(config.token)

if __name__ == "__main__":
    main()
