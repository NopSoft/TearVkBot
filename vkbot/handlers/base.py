from vkwave.bots import SimpleBotEvent

from loguru import logger
from vkbot.bot import bot


@bot.message_handler(bot.command_filter("тест"))
def echo(event: SimpleBotEvent) -> str:
    logger.info("Test handler is work.")
    return "test"
