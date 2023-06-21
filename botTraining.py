import telebot
from telebot import types
bot = telebot.TeleBot("6074049396:AAFTzxESww-VKyVMcPef1lnhDxc-UOk34bs")

@bot.message_handler(commands={'start'})
def start(message):
     markup = types.ReplyKeyboardMarkup()
     kpoi1 =types.KeyboardButton('Посмотреть прайс')
     markup.row(kpoi1)
     kpoi2 = types.KeyboardButton('Записаться')
     kpoi3 = types.KeyboardButton('Вернуться назад')
     markup.row(kpoi2, kpoi3)
     bot.send_message(message.chat.id, 'Выбери что тебе интересно и нажми на кнопку!', reply_markup = markup)
     bot.register_next_step_handler(message, on_click)
     
def on_click(message):
    if message.text == 'Посмотреть прайс':
        bot.send_message(message.chat.id, 'Группа/8занятий/месяц 5 000,00 ₽:\n Обонемент/8занятий 14 400,00 ₽:\n Разовая 2 500,00 ₽:\n Обонемент2/4занятия 8 000,00 ₽')
        
   
bot.polling(non_stop=True)