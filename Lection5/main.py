""" from isOdd import isOdd # проверка четности
print(isOdd(1))
print(isOdd(4))
 """

""" import time # имитация загрузки
from progress.bar import Bar

bar = Bar('Processing', max=20)
for i in range(20):
    time.sleep(0.1)
    bar.next()
bar.finish() """

""" import emoji # библтотека эмоджи

print(emoji.emojize('Python is :thumbs_up:')) """


""" import matplotlib.pyplot as plt
import numpy as np
list = [1, 2, 3, 2, 7]
plt.plot(list)
plt.show() """

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands as bot
#from bot_commands import * # импортировать все




app = ApplicationBuilder().token("5629640823:AAGNiW-uQuWHzZibfwWL0IQ26uEYoitJ8VI").build()

app.add_handler(CommandHandler("hi", bot.hi_command))
app.add_handler(CommandHandler("time", bot.time_command))
app.add_handler(CommandHandler("help", bot.help_command))
app.add_handler(CommandHandler("sum", bot.sum_command))
print('server START')
app.run_polling()
