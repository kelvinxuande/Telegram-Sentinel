# Main python script for 'Telegram Chat Sentinel'
# Created by Kelvin Tan

# Do necessary imports:
from telethon import TelegramClient, sync, events
from telethon.tl.types import InputChannel
import logging
import sys
import yaml

# Start of main code:
def start(config):
    # Get information from config file:
    session_name = config["session_name"]
    api_id = config["api_id"]
    api_hash = config["api_hash"]
    trigger_words = config["trigger_words"]
    quit_key_words = config["quit_key_words"]
    
    # Initialisations:
    input_channels_entities = []
    output_channel_entity = None
    connectivity = ()
    # Acquire entities:
    with TelegramClient(session_name, api_id, api_hash) as client:
        for d in client.iter_dialogs():
            if d.name in config["input_channel_names"]:
                input_channels_entities.append( InputChannel(d.entity.id, d.entity.access_hash) )
            if d.name == config["output_channel_name"]:
                output_channel_entity = InputChannel(d.entity.id, d.entity.access_hash)
        
        # Do a check on entities acquired:
        if output_channel_entity is None:
            connectivity = connectivity + (0,)
            print("Requested output channel entity could not be found")
        else:
            connectivity = connectivity + (1,)
        if len(input_channels_entities) == 0:
            connectivity = connectivity + (0,)
            print("Requested input channel entity(s) cannot be found")
        else:
            connectivity = connectivity + (1,)
        if 0 in connectivity:
            print("Shutting down due to entity-check failure...")            
            sys.exit(1)
        else:
            print("Entity-check successful!")
            print("Listening on %d channels. Forwarding messages to %s." %(len(input_channels_entities), config['output_channel_name']))
        
        # Create events to listen to:
        # For more recipes, visit https://arabic-telethon.readthedocs.io/en/stable/
        
        @client.on(events.NewMessage(chats=input_channels_entities))
        async def forwarding_handler(event):
            client = event.client
            # if trigger_words in event.raw_text.lower():
            if any(word in event.raw_text.lower() for word in trigger_words):
                # await event.reply('hi!')    # extra
                await client.forward_messages(output_channel_entity, event.message)
        
        @client.on(events.NewMessage(chats=output_channel_entity, outgoing = True))
        async def control_handler(event):
            # if quit_key_words in event.raw_text.lower():
            if any(word in event.raw_text.lower() for word in quit_key_words):
                await client.disconnect()
        
        client.run_until_disconnected()

# load config file and start script:
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} CONFIG_PATH")
        sys.exit(1)
    with open(sys.argv[1], 'rb') as f:
        config = yaml.load(f)
    start(config)
    
