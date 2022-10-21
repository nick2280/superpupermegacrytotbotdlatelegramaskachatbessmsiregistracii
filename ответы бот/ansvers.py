import telebot
import config
from telebot import types
from perem import p0, aboutus, gar, mor, bu, con, insr

a = 0

bot = telebot.TeleBot(config.TOKEN)

joinedFile = open(r"joined.txt" )
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()

@bot.message_handler(commands=['start'])
def start(message):
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("joined.txt",'w')
        joinedFile.write(str(message.chat) + "\n")
        joinedUsers.add(str(message.chat.id))



        global a
        a += 1
        print (a)

    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("О НАС💁‍", callback_data = 'about')
    markup.add(button1)
    button2 = types.InlineKeyboardButton("О ПРОЕКТЕ 🤖", callback_data = 'aboutprog')
    markup.add(button2)
    button3 = types.InlineKeyboardButton("✅ГАРАНТИИ✅‍", callback_data = 'garant')
    markup.add(button3)
    button4 = types.InlineKeyboardButton("ℹ️ДОП.ИНФОРМАЦИЯℹ️", callback_data = 'more')
    markup.add(button4)
    button5 = types.InlineKeyboardButton("💲ПОКУПКА💲‍", callback_data = 'buy')
    markup.add(button5)
    button6 = types.InlineKeyboardButton("🚛СВЯЗЬ С НАМИ🚛", callback_data = 'connect')
    markup.add(button6)

    bot.send_message(message.chat.id, '⬇️ГЛАВНОЕ МЕНЮ⬇️', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    markup = types.InlineKeyboardMarkup()
    button7 = types.InlineKeyboardButton("⏪ВЕРНУТЬСЯ⏪‍", callback_data = 'back')
    button8 = types.InlineKeyboardButton("🔔ОБРАТНАЯ СВЯЗЬ🔔‍", url = 'https://t.me/pay_anserversrobot?start=feedback')
    button9 = types.InlineKeyboardButton( '❇️ИНСТРКУЦИЯ❇️', callback_data =  'intr')
    if call.data == "about":
        markup.add(button7)
        bot.send_message(call.message.chat.id, aboutus, reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id  )

    elif call.data == "aboutprog":
        markup.add(button7)
        bot.send_message(call.message.chat.id, p0, reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id  )
    elif call.data == "garant":
        markup.add(button7)
        bot.send_message(call.message.chat.id, gar, reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id  )
    elif call.data == "more":

        markup.add(button7)
        bot.send_message(call.message.chat.id, mor, reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id  )
    elif call.data == "buy":

        markup.add(button9)
        markup.add(button7)
        bot.send_message(call.message.chat.id, bu, reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id  )
    elif call.data == "connect":
        markup.add(button8)
        markup.add(button7)
        bot.send_message(call.message.chat.id, con, reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id  )
    elif call.data == "intr":
        markup.add(button7)

        bot.send_message(call.message.chat.id, insr, reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id  )
    elif call.data == 'back':

        button1 = types.InlineKeyboardButton("О НАС💁‍", callback_data = 'about')

        button2 = types.InlineKeyboardButton("О ПРОЕКТЕ 🤖", callback_data = 'aboutprog')

        button3 = types.InlineKeyboardButton("✅ГАРАНТИИ✅‍", callback_data = 'garant')

        button4 = types.InlineKeyboardButton("ℹ️ДОП.ИНФОРМАЦИЯℹ️", callback_data = 'more')

        button5 = types.InlineKeyboardButton("💲ПОКУПКА💲‍", callback_data = 'buy')

        button6 = types.InlineKeyboardButton("🚛СВЯЗЬ С НАМИ🚛", callback_data = 'connect')

        markup.add(button1, button2  )
        markup.add(button3, button4)
        markup.add (button5, button6)

        bot.send_message(call.message.chat.id, "Вы вернулись в меню",reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id  )

@bot.message_handler(commands=['secret'])
def send(message):
    for user in joinedUsers:
        bot.send_message(user, message.text[message.text.find(' '):])


@bot.message_handler(commands=['user'])
def send (message):
        global a

        bot.send_message(message.chat.id,  a )

##
bot.polling(none_stop=True, interval=0)



