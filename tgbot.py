import telebot
import random
from telebot import types

spis = ''

# Создаем бота
bot = telebot.TeleBot('5563802554:AAF7xLtdvIyB8I87zDzViqlMLsF0nCxKtxA')
# Команда start      python Bot.py
@bot.message_handler(commands=['start'])
def start(m, res=False):
        # Добавляем две кнопки
        global spis
        spis = ''
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Список")
        item2=types.KeyboardButton("+")
        item3 = types.KeyboardButton("-")
        markup.add(item1, item2, item3)
        #markup.add(item2)
        #markup.add(item3)

        bot.send_message(m.chat.id, "Игра в 20:30 в среду. Больше людей - меньше цена")
        bot.send_message(m.chat.id,'Пойдешь?', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    global spis
    if message.text.strip() == '+':
        if message.from_user.username not in spis:
            answer = (f"Пользователь {message.from_user.username} записан на игру")
            spis +='@'+str(message.from_user.username) +"\n"
        else:
            answer = (f'Пользователь {message.from_user.username} уже есть в списке')

    elif message.text.strip() == '-':
        if message.from_user.username in spis:
            answer = (f"Пользователь {message.from_user.username} вычеркнут из списка")
            spis = spis.replace('@'+str(message.from_user.username)+'\n', '')
        else:
            answer = (f'Пользователь {message.from_user.username} еще не записан, чтобы быть вычеркнутым из списка')

    elif message.text.strip().lower() == 'список':
        m = spis
        answer = (f"Список добровольцев: \n{m}")
    else:
        answer = ''
    # Отсылаем юзеру сообщение в его чат    '''", message.chat.username, '''
    if answer != '':
        bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True, interval=0)
