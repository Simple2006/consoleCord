import discord, time, asyncio

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

    async def on_ready(self):
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
        print(f"{color.RED + '1. Send Message to Channel | 2. Send DMs' + color.END}")
        global choice
        choice = int(input("\nSelect Choice: "))
        if choice == 1:
            global channelId
            channelId = input("\nEnter Channel Id: ")
            channelId = channelId.strip()
            channelId = int(channelId)
        if choice == 2:
            global userId
            userId = input("\nEnter User Id to DM: ")
            userId = userId.strip()
            userId = int(userId)

        while True:
            message = input("Enter message: ")
            if choice == 1:
                channel = client.get_channel(channelId)
                await channel.send(f"{message}")
            elif choice == 2:
                channel = client.get_channel(userId)
                await channel.send(f"{message}")


client = MyClient()
client.run("", bot = False)
