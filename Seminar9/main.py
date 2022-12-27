from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands as bot
#from bot_commands import * # импортировать все




app = ApplicationBuilder().token("YOU TOKKEN TELEGRAMM").build()

app.add_handler(CommandHandler("hi", bot.hi_command))
app.add_handler(CommandHandler("time", bot.time_command))
app.add_handler(CommandHandler("help", bot.help_command))
app.add_handler(CommandHandler("sum", bot.sum_command))
print('server START')
app.run_polling()
