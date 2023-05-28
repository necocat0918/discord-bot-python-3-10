import discord
import responses


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'YOUR TOKEN HERE'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    from discord import Game, ActivityType

    @client.event
    async def on_ready():
        activity = Game(name="Example Activity", type=ActivityType.playing)
        await client.change_presence(activity=activity)
        print(f'{client.user} is now running!')


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?' and channel == 'any-channel':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            if channel == 'chat-with-neco' :
               await send_message(message, user_message, is_private=False)

    client.run('YOUR TOKEN HERE')
