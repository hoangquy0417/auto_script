import telegram
import os
from dotenv import load_dotenv, dotenv_values
import asyncio

load_dotenv()
BOT = telegram.Bot(token=os.getenv("BOT_TOKEN"))
CHAT_ID = os.getenv("CHAT_ID")


async def send_message(text, chat_id):
    async with BOT:
        await BOT.send_message(text=text, chat_id=chat_id)


async def send_document(document, chat_id):
    async with BOT:
        await BOT.send_document(document=document, chat_id=chat_id)


async def send_photo(photo, chat_id):
    async with BOT:
        await BOT.send_photo(photo=photo, chat_id=chat_id)


async def send_video(video, chat_id):
    async with BOT:
        await BOT.send_video(video=video, chat_id=chat_id)


async def main():
    # Sending a message
    await send_message(text='Hi Quý!, How are you?', chat_id=CHAT_ID)

    # Sending a document
    #await send_document(document=open('/path/to/document.pdf', 'rb'), chat_id=chat_id)

    # Sending a photo
    #await send_photo(photo=open('/path/to/photo.jpg', 'rb'), chat_id=chat_id)

    # Sending a video
    #await send_video(video=open('path/to/video.mp4', 'rb'), chat_id=chat_id)


if __name__ == '__main__':
    asyncio.run(main())
