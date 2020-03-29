##C45 Bot for the c45 discord server
# TODO:
# * Add functionality to access bnet
# * Add functionality to host files
# * Add functionality to play songs
# * Add reminders (bot will message if something is due)
# * Welcome messgaes and role assignment
import discord
from discord.ext import commands
import os
import subprocess

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        guilds = []
        async for guild in self.fetch_guilds():
            print(guild)
            guilds.append(guild)
        c45 = guilds[0]
        channels = await c45.fetch_channels()
        banter = None
        for channel in channels:
            if channel.id==615645678147862538:
                banter = channel
                self.banter = banter
                break
       

    async def on_message(self, message):
        # Ignore messages from the bot
        if message.author == self.user:
            return
        else:
            # Messages from everyone else
            if message.content.startswith(">"):
                # Remove the `>`
                command = message.content[1:].strip()
                print("Got command: \"" + command + "\"")

                if command.lower() == "ip:route":
                    await message.channel.send(subprocess.getoutput("route"))
                elif command.lower() == "ip:if":
                    await message.channel.send(subprocess.getoutput("ifconfig"))
                elif command.lower() == "ip:arp":
                    await message.channel.send(subprocess.getoutput("arp"))
                elif command.startswith("ls"):
                    dirLS = command[2:]
                    await message.channel.send(subprocess.getoutput("ls " + dirLS))
                elif command.lower().startswith("ip:ping"):
                    ip = command[7:]
                    await message.channel.send(subprocess.getoutput("ping " + ip + " -c 3"))
                elif command.lower().startswith("ip:trace"):
                    ip = command[8:]
                    await message.channel.send(subprocess.getoutput("traceroute " + ip))        
                elif command.lower().startswith("fetch"):
                    import requests
                    url = command[5:]
                    body = requests.get(url).text
                    await message.channel.send(body)
                elif command == "brink":
                    await message.channel.send("EXACTLY - Old Khaki.com")
            elif "test" in message.content.lower():
                # get the id
                id = message.author.id
                print("ID is: " + str(id))

                await message.channel.send("Marks out")
                await message.channel.send("?")
            else:
                print("Message dropped, not a command")
            

client = MyClient()
client.run(os.getenv("C45_Token"))