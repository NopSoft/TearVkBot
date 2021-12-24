from vkwave.bots import SimpleLongPollBot
from loguru import logger
from config import bot_settings

bot = SimpleLongPollBot(tokens=bot_settings["TOKEN"],
                        group_id=bot_settings["GROUP_ID"])


if __name__ == '__main__':
    # Импортируем все хендлеры пакета, чтобы их увидели
    from handlers import *
    logger.info("Start vkbot")
    bot.run_forever()
    logger.info("The vkbot is turned off")
