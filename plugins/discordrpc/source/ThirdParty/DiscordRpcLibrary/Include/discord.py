from pypresence import Presence
import time
import threading
import asyncio

def run_discord_rpc():
    client_id = '1088908938205999194'
    RPC = Presence(client_id)
    RPC.connect()
    button1 = {"label": "GitHub", "url": "https://github.com/MooManisLoud/PyWWW"}
    RPC.update(state="On GitHub", details="Download faster with PyWWW", large_image="bigimage", large_text="Pyinstaller", buttons=[button1], start=time.time())

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    while True:
        try:
            RPC.update()
        except Exception as e:
            print(f"Error updating Discord RPC: {e}")
        time.sleep(15)

# start a new thread to run the Discord RPC code
discord_thread = threading.Thread(target=run_discord_rpc)
discord_thread.start()
