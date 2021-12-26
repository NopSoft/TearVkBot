from vkwave.bots import SimpleBotEvent
from vkwave.bots import (PhotoUploader,)

from io import BytesIO

from loguru import logger

from vkbot.bot import bot
from vkbot.utils import pillow_draw_text
from vkbot import config

from PIL import Image

photo_uploader = PhotoUploader(api_context=bot.api_context)


@bot.message_handler(bot.command_filter("meme"))
async def fresko_meme(event: SimpleBotEvent):
    image = Image.open((config.MEDIA_DIR / "Jak_fresko.jpg").__str__())

    try:
        text = event.object.object.message.reply_message.text
    except AttributeError:
        logger.warning(f"User<{event.from_id}> don`t answer message.")
        text = "Нужно ответить на какое-то сообщение, чтобы появился этот " \
               "текст тупой ты кусок дерьма"

    draw_img = pillow_draw_text.write_in_image(
        image, text, xy=(100, 100), width=650, height=574
    )

    by = BytesIO()
    draw_img.save(by, format="JPEG")
    by.seek(0)

    resp = await photo_uploader.get_attachment_from_io(peer_id="0",
                                                       f=by,
                                                       file_extension="JPEG")

    logger.info(f"User<{event.from_id}> get image meme Jak Fresko")
    await event.answer(attachment=resp, message="Фрескоооооо")

