"""Telegram front end for offline IP classification."""

import os

from iptools import inspect_ip


def main() -> None:
    token = os.getenv("BOT_TOKEN", "")
    if not token:
        raise RuntimeError("Set BOT_TOKEN before starting the bot.")
    import telebot

    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start(message) -> None:
        bot.reply_to(message, "Send one IPv4 or IPv6 address for offline classification.")

    @bot.message_handler(func=lambda message: True)
    def handle_address(message) -> None:
        try:
            result = inspect_ip(message.text or "")
        except ValueError:
            bot.reply_to(message, "Please send a valid IPv4 or IPv6 address.")
            return
        details = "\n".join(f"{key}: {value}" for key, value in result.items())
        bot.reply_to(message, details)

    bot.infinity_polling()


if __name__ == "__main__":
    main()
