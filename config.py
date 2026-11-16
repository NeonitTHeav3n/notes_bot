import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError(
        "Не задана переменная окружения BOT_TOKEN.\n"
        "Задайте её перед запуском:\n"
        "  Windows cmd:      set BOT_TOKEN=123456:AA...\n"
        '  PowerShell:       $env:BOT_TOKEN="123456:AA..."\n'
        "  Linux / macOS:    export BOT_TOKEN=123456:AA...\n"
        "Токен выдаёт @BotFather в Telegram (команда /mybots)."
    )
