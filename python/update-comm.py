import random
import telebot
import time
bot = telebot.TeleBot('5654569004:AAHcuDRp2WBQGwvnozQxA_azihaTgBU5Ruo')
from telebot import types
first = ["Сегодня — идеальный день для новых начинаний.",
         "Оптимальный день для того, чтобы решиться на смелый поступок!",
         "Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.",
         "Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.",
         "Плодотворный день для того, чтобы разобраться с накопившимися делами."]
second = ["Но помните, что даже в этом случае нужно не забывать про", "Если поедете за город, заранее подумайте про",
          "Те, кто сегодня нацелен выполнить множество дел, должны помнить про",
          "Если у вас упадок сил, обратите внимание на",
          "Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]
second_add = ["отношения с друзьями и близкими.",
              "работу и деловые вопросы, которые могут так некстати помешать планам.",
              "себя и своё здоровье, иначе к вечеру возможен полный раздрай.",
              "бытовые вопросы — особенно те, которые вы не доделали вчера.",
              "отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]
third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.",
         "Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.",
         "Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.",
         "Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.",
         "Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]
monetka = ["ПОБЕДА", "ПРОИГРЫШ"]
kubik = ['ТЕБЕ ВЫПАЛО 1', 'ТЕБЕ ВЫПАЛО 2', 'ТЕБЕ ВЫПАЛО 3', 'ТЕБЕ ВЫПАЛО 4', 'ТЕБЕ ВЫПАЛО 5', 'ТЕБЕ ВЫПАЛО 6',
         '😨КУБИК ВСТАЛ НА РЕБРО😨']

joinedFile = open(r"C:/python/joined.txt" )
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()

@bot.message_handler(commands=['start'])
def start(message):
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("C:/python/joined.txt",'w')
        joinedFile.write(str(message.chat) + "\n")
        joinedUsers.add(str(message.chat.id))
        bot.send_message(message.chat.id, "made by @Qwerkinlore")
        bot.send_message(message.chat.id, '/help - сводка команд')
                         
@bot.message_handler(commands=['help'])
def send(message):
    bot.send_message(message.chat.id, '/start - Начать \n /goroscop - гороскоп \n /monetka - игра в монетку \n /kubik - бросить кубик')


@bot.message_handler(commands=['secretsendall'])
def send(message):
    for user in joinedUsers:
        bot.send_message(user, message.text[message.text.find(' '):])
@bot.message_handler(commands=['goroscop'])
def send(message):
    bot.send_message(message.chat.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня. ")
    keyboard = types.InlineKeyboardMarkup()
    key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')

    keyboard.add(key_oven)
    key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')
    keyboard.add(key_telec)
    key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')
    keyboard.add(key_bliznecy)
    key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
    keyboard.add(key_rak)
    key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
    keyboard.add(key_lev)
    key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')
    keyboard.add(key_deva)
    key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')
    keyboard.add(key_vesy)
    key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')
    keyboard.add(key_scorpion)
    key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')
    keyboard.add(key_strelec)
    key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')
    keyboard.add(key_kozerog)
    key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')
    keyboard.add(key_vodoley)
    key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')
    keyboard.add(key_ryby)

    bot.send_message(message.chat.id, text='Выбери свой знак зодиака', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "zodiac":
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(
            second_add) + ' ' + random.choice(third)
       
        bot.send_message(call.message.chat.id, msg)




@bot.message_handler(commands=['monetka'])
def send(message):
    mon = random.choice(monetka) + ' '
    bot.send_message(message.chat.id, mon)

@bot.message_handler(commands=['kubik'])
def send(message):
    kub = random.choice(kubik) + ' '
    bot.send_message(message.chat.id, kub)


bot.polling(none_stop=True, interval=0)
