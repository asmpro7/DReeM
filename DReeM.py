# DReeM script
# made by asmpro
# date: 24/3/2023
# TG:@asmprotk

from telethon import TelegramClient
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from rich.console import Console
from tqdm.auto import tqdm
import os

Console().print(
    f"Welcome to [cyan]DReeM[/] Script to download media from Telegram\n ([red italic]If it your first time choose Settings[/])\n", style="bold green")
Console().print(
    "1) [yellow1]media from group you are in[/]\n2) [yellow1]Settings[/]\n", style="bold")

user_cho = int(input("Enter your choose: "))
if user_cho == 1:
    pass
elif user_cho == 2:
    pathF = 'api.txt'
    os.system(f"notepad.exe {pathF}")
else:
    Console().print("Please enter a vaild choose", style="bold red")
post_link = input("Enter the post link to download: ").split("/")
chan_id = post_link[-2]
msg_id = int(post_link[-1])
if chan_id.isdigit():
    chan_id = int(chan_id)
print("\n")
apiData = open("api.txt", "r")
apiList = apiData.readlines()

api_id = int(apiList[0].splitlines()[0].split(":")[1])
api_hash = apiList[1].splitlines()[0].split(":")[1]
client = TelegramClient("session", api_id, api_hash)
client.start()
apiData.close()

#################################


def callback(current, total):
    global pbar
    global prev_curr
    pbar.update(current-prev_curr)
    prev_curr = current
#################################


async def main():
    ###########
    global pbar
    global prev_curr
    ###########
    message = await client.get_messages(PeerChannel(chan_id), ids=msg_id)
    if message.media:
        ###############################################################
        prev_curr = 0
        pbar = tqdm(total=message.file.size, unit='B', unit_scale=True)
        ###############################################################
        path = await client.download_media(message, progress_callback=callback)
        pbar.close()  # <<<<<<<###########
        Console().print(
            f"\nFile saved as [cyan italic underline]{path}[/]", style="bold green")
    else:
        Console().print("Message didn't contain any media!", style="bold red")
    Console().print("\nDReeM script by asmpro", style="bold red")
with client:
    client.loop.run_until_complete(main())
