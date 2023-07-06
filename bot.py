from telethon.sync import TelegramClient
from telethon.tl import functions, types

import random
import string

api_id =
api_hash =''
phone_number = 
owner_id = 
username = ''
title = ''
short_name = ''

emojis = True

stickers = [
    {
        'file_id': 'file_id_1',
        'access_hash': 'access_hash_1',
        'file_reference': 'file_reference_1',
        'emoji': '😀',
        'file_path': './pic.png'
    },
]

def generate_file_reference():
    length = 16  # Adjust the length of the file reference as needed
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def create_emoji_stickerset(username, api_id, api_hash, phone_number, owner_id, title, short_name, stickers, emojis ):
    client = TelegramClient('ASavs', api_id, api_hash)
    client.connect()
    
    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        code = input('paste code: ')
        client.sign_in(phone_number, code)
    print('hi')
    # Upload sticker images and obtain the necessary file details
    uploaded_files = []
    for sticker in stickers:
        uploaded_file = client.upload_file(sticker['file_path'])
        uploaded_files.append(uploaded_file)
    
    # Create the sticker items for the set
    sticker_items = []
    for i, sticker in enumerate(stickers):
        print(uploaded_files[i])
        rr = generate_file_reference()
        sticker_item = types.InputStickerSetItem(
            document=types.InputDocument(
                id=uploaded_files[i].id,
                access_hash=uploaded_files[i].id,
                file_reference=rr
            ),
            emoji=sticker['emoji'],
        )
        print(sticker_item.to_dict())
        sticker_items.append(sticker_item)
    
    # Create the sticker set
    result = client(functions.stickers.CreateStickerSetRequest(
        user_id=username,
        title=title,
        short_name=short_name,
        stickers=sticker_items,
        emojis=emojis,
    ))
    print(result)
    


if __name__ == '__main__':
    create_emoji_stickerset(username, api_id, api_hash, phone_number, owner_id, title, short_name, stickers, emojis)