
# Импорт библиотек и регестрация бота
import telebot
from telebot import types
import asana
import config

Token = config.Token
AsanaToken = config.AsanaToken
taskproject = config.taskproject
workspace_id = config.workspace_id
hi_msg = config.hi_msg

bot = telebot.TeleBot(Token)
client = asana.Client.access_token(AsanaToken)
# ?a = client.projects.find_all( workspace=workspace_id)
# for e in a:
# print(list(client.projects.find_all(workspace_id)))

#Основные переменные
hostel = ''
room = ''
trouble = ''

a = {}

#Инициализация рабочего места 
# myspaces = client.list_workspaces()
# myproject = client.get_project(taskproject)
# workspaces = client.workspaces.find_all()
# print(list(workspaces))


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('/start')
    #item1 = types.KeyboardButton('Инструкции')
    item2 = types.KeyboardButton('Заявка')
    keyboard.add(item2)
    bot.send_message(message.chat.id, hi_msg, reply_markup=keyboard)


@bot.message_handler(content_types = ['text'])
def bot_message(message):
    # print(0)
    if message.chat.type == 'private':
        """"
        if message.text == 'Инструкции':
            # print(1)
            bot.send_message(message.chat.id, 'инструкции')
            bot.register_next_step_handler(message, start_message)
        """
        if message.text == 'Заявка':
            bot.send_message(message.chat.id, 'Введите номер общежития')
            bot.register_next_step_handler(message, call_hostel)


def call_hostel(message):
    hostel = message.text
    key = str(message.chat.id)
    a[key] = [hostel]
    bot.send_message(message.from_user.id, "Введите номер комнаты")
    bot.register_next_step_handler(message, call_room)


def call_room(message):
    room = message.text
    key = str(message.chat.id)
    a[key].append(room)
    bot.send_message(message.from_user.id, "Какая у вас проблема?")
    bot.register_next_step_handler(message, call_trouble)
    return room


def call_trouble(message):
    print("hostel: ", hostel, type(hostel))
    print('room: ', room, type(room))

    trouble = message.text
    trouble = trouble + ' - t.me/' + str(message.from_user.username)
    key = str(message.chat.id)
    a[key].append(trouble)
    bot.send_message(message.from_user.id, "Спасибо за обращение!")
    result = client.tasks.create_in_workspace(workspace_id,
                                              {'name': a[key][0] + '_' + a[key][1],
                                               'notes': a[key][2],
                                               'projects': [taskproject]})
    bot.register_next_step_handler(message, start_message)
    del a[key]



bot.polling(none_stop = True)
