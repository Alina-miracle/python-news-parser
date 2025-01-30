from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext


# Функция приветствия
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Привет! Я бот для парсинга новостей. Используй команду /help ")


# Функция помощи
async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "/start - Приветствие\n/help - Справка по командам\n/parse - Запуск парсера\n/result - Результаты парсинга")


# Функция для запуска парсера
async def parse(update: Update, context: CallbackContext) -> None:
    query = ' '.join(context.args)  # Получаем параметр из команды
    await update.message.reply_text(f"Запускаем парсер для запроса: {query}")
    # Здесь будет код для запуска парсера (например, из другого файла с парсером)
    # get_news(query)
    await update.message.reply_text("Парсинг завершён.")


# Функция для вывода результатов парсинга
async def result(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Вот результаты парсинга: [тут будут данные]")


def main() -> None:
    # Твой токен
    application = Application.builder().token("7921108720:AAF4tb6RPJZdlq41ZisM0JFtkzbbNEVuhLo").build()

    # Команды
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("parse", parse))
    application.add_handler(CommandHandler("result", result))

    # Запуск бота
    application.run_polling()


if __name__ == '__main__':
    main()
