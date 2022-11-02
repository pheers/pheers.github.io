from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = "1375350998:AAFCKADUqsB5k-wfd5tcf4JvtXAslk46JwE"

web_app = types.WebAppInfo(url = 'https://pheers.github.io/')

keyboard = types.ReplyKeyboardMarkup(
    keyboard = [
        [types.KeyboardButton(text = "Записаться", web_app = web_app)]
        ],
        resize_keyboard = True
)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start'])
async def start(message):
    await bot.send_message(message.chat.id,
    "Лови кнопку",
    reply_markup = keyboard

    )

@dp.message_handler(content_types="web_app_data") #получаем отправленные данные 
def answer(webAppMes):
    data = webAppMes.web_app_data.data #конкретно то что мы передали в бота
    data = data.split(',')
    dict = {}
    for p in data:
        dict[p.split(":")[0]] = p.split(":")[1]
    
    bot.send_message(webAppMes.chat.id, f"ФИО: {dict[last_name]} {dict["name"]} {dict["third_name"]} \nТелефон: {dict['phone']}") 
   #отправляем сообщение в ответ на отправку данных из веб-приложения 

if __name__ == '__main__':
    executor.start_polling(dp)