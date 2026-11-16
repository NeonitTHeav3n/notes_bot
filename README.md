# notes_bot — Telegram-бот для заметок

Бот на **aiogram 3** с хранением заметок в SQLite: создание, просмотр и удаление заметок
прямо в чате. Демонстрирует работу с асинхронным Telegram Bot API, роутерами-хендлерами
и SQLite через `sqlite3`.

*EN summary: a small async Telegram notes bot built with aiogram 3 and SQLite.*

## Возможности

- команды бота: заметки создаются и читаются из чата;
- хранение в SQLite (`notes.db` создаётся автоматически при первом запуске);
- токен не хранится в коде — только в переменной окружения.

## Структура

```
notes_bot/
├── notes_bot/
│   ├── bot.py         # точка входа: Bot, Dispatcher, polling
│   ├── config.py      # чтение BOT_TOKEN из окружения
│   ├── handlers.py    # роутер и хендлеры команд
│   └── database.py    # SQLite: создание таблицы, CRUD
├── requirements.txt
├── .gitignore
└── README.md
```

## Запуск

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate.bat
pip install -r requirements.txt
```

Токен берётся у [@BotFather](https://t.me/BotFather) (`/mybots` → твой бот → API Token) и задаётся
в переменной окружения — **в коде его быть не должно**:

```bash
# Windows cmd
set BOT_TOKEN=123456:AA...

# PowerShell
$env:BOT_TOKEN="123456:AA..."

# Linux / macOS
export BOT_TOKEN=123456:AA...
```

Запуск (важно: из папки `notes_bot`, потому что импорты плоские — `from config import BOT_TOKEN`):

```bash
cd notes_bot
python bot.py
```

В консоли появится `Бот запущен...` — можно писать боту в Telegram.

## Безопасность

- `.env`, `*.db`, `__pycache__/` — в `.gitignore`;
- токен читается из окружения; при утере — отозвать в BotFather и выпустить новый;
- если токен когда-либо попадал в git-историю, её нужно переписать: недостаточно просто удалить файл.
