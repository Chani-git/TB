# Импорт библиотек и регистрация бота
import telebot
from telebot import types
import asana
import config
from common import AsanaTicket

Token = config.Token
AsanaToken = config.AsanaToken
taskproject = config.taskproject
workspace_id = config.workspace_id
hi_msg = config.hi_msg
bay_msg = config.bay_msg
cant_make_a_ticket = config.cant_make_a_ticket
partial_ticket = config.particial_ticket

bot = telebot.TeleBot(Token)
client = asana.Client.access_token(AsanaToken)

task_in_work = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('/start')
    # item1 = types.KeyboardButton('Инструкции')
    item2 = types.KeyboardButton('Заявка')
    keyboard.add(item2)
    bot.send_message(message.chat.id, hi_msg, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        """"
        if message.text == 'Инструкции':
            # print(1)
            bot.send_message(message.chat.id, 'инструкции')
            bot.register_next_step_handler(message, start_message)
        """
        if message.text == 'Заявка':
            issue = AsanaTicket()
            task_in_work[message.chat.id] = issue
            bot.send_message(message.chat.id, 'Введите номер общежития \n\n Input hostel number')
            bot.register_next_step_handler(message, call_hostel)


def call_hostel(message):
    task_in_work[message.chat.id].hostel = message.text
    bot.send_message(message.from_user.id, "Введите номер комнаты\n\n Input room number")
    bot.register_next_step_handler(message, call_room)


def call_room(message, ):
    task_in_work[message.chat.id].room = message.text
    bot.send_message(message.from_user.id, "Опишите свою проблему\n\nAsk you question")
    bot.register_next_step_handler(message, call_trouble)


def call_trouble(message):
    task_in_work[message.chat.id].trouble = message.text + '\n' + 'https://t.me/' + str(message.from_user.username)


def create_ticket(message):
    if task_in_work[message.chat.id].hostel and task_in_work[message.chat.id].room and task_in_work[message.chat.id].trouble:
        if task_in_work[message.chat.id].create_task(client, workspace_id, taskproject):
            bot.register_next_step_handler(message, start_message)
            bot.send_message(message.from_user.id, bay_msg)
        else:
            bot.send_message(message.from_user.id, cant_make_a_ticket)
    else:
        bot.send_message(message.from_user.id, partial_ticket)
        bot.register_next_step_handler(message, bot_message)


bot.polling(none_stop = True)


# while True:
#     try:
#         bot.polling(none_stop = True)
#     except:
#         print("restart\n")
