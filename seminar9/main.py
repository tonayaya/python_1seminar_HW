from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler
from random import randint
import functions

# 1) Напишите Бота, удаляющего из текста все слова, содержащие "абв". (Ввод от пользователя)
# 2) Создайте Бота для игры с конфетами человек против бота. (Дополнительно)



app = ApplicationBuilder().token("5801378497:AAGDg-L8eFJNMPsqo57l-kVuXgJ5dmuCpF8").build()

app.add_handler(ConversationHandler(entry_points= [CommandHandler("game", functions.game)], 
                                    states={functions.my_turn:[MessageHandler(filters.TEXT, functions.gamer_turn)],functions.bot:[MessageHandler(filters.TEXT, functions.bot_turn)]},
                                    fallbacks=[CommandHandler("cancel", functions.cancel)]))

app.add_handler(CommandHandler("hello", functions.hello))
app.add_handler(MessageHandler(filters.TEXT, functions.del_word))


app.run_polling()