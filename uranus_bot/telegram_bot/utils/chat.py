""" Xiaomi Geeks Telegram Bot chat utilities"""

from telethon.tl.types import User, ChannelParticipantsAdmins

from uranus_bot import TG_BOT_ADMINS


async def is_group_admin(event) -> bool:
    """Check if a use is an admin"""
    admins = await event.client.get_participants(event.chat_id,
                                                 filter=ChannelParticipantsAdmins)
    try:
        return bool([i for i in admins
                     if event.message.sender_id == i.id
                     or event.message.sender.id in TG_BOT_ADMINS])
    except AttributeError:
        return bool([i for i in admins
                     if i and (event.input_sender.user_id == i.id
                               or event.input_sender.user_id in TG_BOT_ADMINS)])


async def get_user_info(event) -> dict:
    """Returns a dictionary of user information"""
    chat_type = "user" if event.is_private else "group" if event.is_group else "channel"
    chat = await event.get_chat()
    if isinstance(chat, User):
        sender = await event.get_sender()
        name = ''
        if sender.first_name:
            name += sender.first_name.strip()
        if sender.last_name:
            name += ' ' + sender.last_name.strip()
        username = sender.username if sender.username else None
        chat_id = sender.id
    else:
        name = chat.title
        try:
            username = chat.username if chat.username else None
        except AttributeError:
            username = None
        chat_id = chat.id
    return {'id': chat_id, 'username': username, 'name': name, 'type': chat_type}
