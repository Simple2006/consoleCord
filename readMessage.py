import discord, time, asyncio
import os


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class MyClient(discord.Client):

    print("\x1b[8;50;115t")

    a = ''' 
 $$$$$$\                                          $$\            $$$$$$\                            $$\ 
$$  __$$\                                         $$ |          $$  __$$\                           $$ |
$$ /  \__| $$$$$$\  $$$$$$$\   $$$$$$$\  $$$$$$\  $$ | $$$$$$\  $$ /  \__| $$$$$$\   $$$$$$\   $$$$$$$ |
$$ |      $$  __$$\ $$  __$$\ $$  _____|$$  __$$\ $$ |$$  __$$\ $$ |      $$  __$$\ $$  __$$\ $$  __$$ |
$$ |      $$ /  $$ |$$ |  $$ |\$$$$$$\  $$ /  $$ |$$ |$$$$$$$$ |$$ |      $$ /  $$ |$$ |  \__|$$ /  $$ |
$$ |  $$\ $$ |  $$ |$$ |  $$ | \____$$\ $$ |  $$ |$$ |$$   ____|$$ |  $$\ $$ |  $$ |$$ |      $$ |  $$ |
\$$$$$$  |\$$$$$$  |$$ |  $$ |$$$$$$$  |\$$$$$$  |$$ |\$$$$$$$\ \$$$$$$  |\$$$$$$  |$$ |      \$$$$$$$ |
 \______/  \______/ \__|  \__|\_______/  \______/ \__| \_______| \______/  \______/ \__|       \_______|
                                                                                                    '''
    print(f"{color.BLUE + a + color.END}")


    print(f"{color.RED + '1. Read All | 2. Read Server | 3. Read Channel | 4. Read User | 5. Read DM | 6. Read All DMs' + color.END}")
    global choice
    choice = int(input("\nSelect Choice: "))
    if choice == 2:
        global serverId
        serverId = input("\nEnter Server Id: ")
        serverId = serverId.strip()
        serverId = int(serverId)
    if choice == 3:
        global channelId
        channelId = input("\nEnter Channel Id: ")
        channelId = channelId.strip()
        channelId = int(channelId)
    if choice == 4:
        global userId
        userId = input("\nEnter User Id: ")
        userId = userId.strip()
        userId = int(userId)
    if choice == 5:
        global userDM
        userDM = input("\nEnter User Id: ")
        userDM = userDM.strip()
        userDM = int(userDM)

    async def on_message(self, message):
        #message needs to be sent to activate program!
        if choice == 1:
            try:
                print(f"{message.guild.name}: {color.BOLD + str(message.author) + color.END}: {color.BOLD + str(message.content) + color.END}")
                time.sleep(0.6)
            except:
                pass
        if choice == 2:
            try:
                if message.guild.id == serverId:
                    print(f"{message.author}: {message.content}")
                    time.sleep(0.1)
            except:
                pass
        if choice == 3:
            try:
                if message.channel.id == channelId:
                    print(f"{message.author}: {message.content}")
                    time.sleep(0.1)
            except:
                pass
        if choice == 4:
            try:
                if message.author.id == userId:
                    print(f"{message.author}: {message.content}")
                    time.sleep(0.1)
            except:
                pass
        if choice == 5:
            if message.author.id == userDM and isinstance(message.channel, discord.channel.DMChannel) or message.author == self.user and isinstance(message.channel, discord.channel.DMChannel) and str(await client.fetch_user(userDM)) in str(client.get_channel(message.channel.id)):
                    print(f"{message.author} to {await client.fetch_user(userDM)}: {message.content}")
                    time.sleep(0.1)

        if choice == 6:
            if isinstance(message.channel, discord.channel.DMChannel):
                toWho = str(await client.fetch_channel(message.channel.id))
                toWho = toWho.split("Direct Message")
                toWho = toWho[1].split("with")
                toWho = toWho[1].strip()
                print(f"{message.author} to {toWho}: {message.content}")
                time.sleep(0.3)


client = MyClient()
client.run("", bot = False)