import discord
import re
import config
from piazza_api import Piazza
import html

class Client(discord.Client):
    def __init__(self):
        super(Client, self).__init__()

        # Regex to check if message wants a post
        self.piazza_regex = re.compile(r"(^|\s)p([0-9]+)", re.IGNORECASE)

        # Piazza setup
        p = Piazza()
        p.user_login(config.email, config.password)
        self.network = p.network(config.network)

    async def on_ready(self):
        print("Connected as {}".format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        match = self.piazza_regex.search(message.content)

        if match:
            # Fetch the post
            n = match.group(2)
            post = self.network.get_post(int(n))

            # Find the subject and content of the latest version of the post
            latest = post["history_size"] - 1
            subject = post["history"][latest]["subject"]
            content = post["history"][latest]["content"]

            # Try to remove HTML from content
            content = re.sub('<[^<]+?>', '', content)
            content = html.unescape(content)
            subject = html.unescape(subject)

            # The base of the URL of any post
            url = f"https://piazza.com/class/{config.network}?cid="

            # Construct a pretty embed
            quoted_text = "\n".join([f"> {line}" for line in content[:80].split("\n")])
            e = discord.Embed(
                title=subject,
                description=quoted_text + f"...\n\nTo delete this, <@{message.author.id}> can react with 🗑️.",
                url=url + n,
                color=0xffb862
            )

            reply = await message.reply(embed=e)
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
