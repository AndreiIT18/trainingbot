import telebot
import sqlite3

bot = telebot.TeleBot("6074049396:AAFTzxESww-VKyVMcPef1lnhDxc-UOk34bs")
name = None

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('training.sql')
    cur = conn.cursor()
    
    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), surname varchar(12))')
    conn.commit()
    cur.close()
    conn.close()
    
    bot.send_message(message.chat.id, 'Привет! Сейчас тебя запишем на рренировку! Ввидите ваше имя!')
    bot.register_next_step_handler(message, user_name)
    
def user_name(message):
 global name 
 name = message.text.strip()
 bot.send_message(message.chat.id, 'Фамилию')
 bot.register_next_step_handler(message, surname)

def surname(message):
    password = message.text.strip()
    
    conn = sqlite3.connect('training.sql')
    cur = conn.cursor()
    
    cur.execute('INSERT INTO users (name, surname) VALUES ("%s","%s")' % (name, surname))
    conn.commit()
    cur.close()
    conn.close()
    
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Вы зарегестрированы!',reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def calldack(call):
     conn = sqlite3.connect('training.sql')
     cur = conn.cursor()
    
     cur.execute('SELECT * FROM users')
     users = cur.fetchall()
     
    #  info = ''
    #  for el in users:
    #      info += f'Имя: {el[1]}, Пароль: {el[2]}\n'
     
    #  cur.close()
    #  conn.close()

    #  bot.send_message(call.message.chat.id, info)

bot.polling(non_stop=True)
