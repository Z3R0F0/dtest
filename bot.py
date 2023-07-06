from telethon.sync import TelegramClient
from telethon.tl import functions, types
from telethon.utils import get_attributes

api_id = 
api_hash = ''
phone_number = 
owner_id = 
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


def create_emoji_stickerset(api_id, api_hash, phone_number, owner_id, title, short_name, stickers, emojis):
    client = TelegramClient('ASavs', api_id, api_hash)
    client.connect()

    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        code = input('code')
        client.sign_in(phone_number, code)
    print('hi')
    # Upload sticker images and obtain the necessary file details
    uploaded_files = []
    for sticker in stickers:
        file = client.upload_file(sticker['file_path'])
        attributes, mime_type = get_attributes(file)

        media = types.InputMediaUploadedDocument(
            file=file,
            mime_type=mime_type,
            attributes=attributes
        )

        result = client(functions.messages.UploadMediaRequest(
            peer='me',
            media=media,
        ))
        uploaded_files.append(result)

    # Create the sticker items for the set
    sticker_items = []
    for i, sticker in enumerate(stickers):
        sticker_item = types.InputStickerSetItem(
            document=types.InputDocument(
                id=uploaded_files[i].document.id,
                access_hash=uploaded_files[i].document.access_hash,
                file_reference=uploaded_files[i].document.file_reference
            ),
            emoji=sticker['emoji'],
        )
        sticker_items.append(sticker_item)

    # Create the sticker set
    result = client(functions.stickers.CreateStickerSetRequest(
        user_id='AnnaRetextAI',
        title=title,
        short_name=short_name,
        stickers=sticker_items,
        emojis=emojis,
    ))
    print(result)


if __name__ == '__main__':
    create_emoji_stickerset(api_id, api_hash, phone_number,
                            owner_id, title, short_name, stickers, emojis)
