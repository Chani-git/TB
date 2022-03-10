hi_msg = 'Привет! Я бот КС Бауманец. С помощью меня ты можешь оставить заявку админам общежитий, кто-то из них свяжется' \
         ' с тобой, чтобы помочь тебе подключиться к интернету. Нажмите "Заявка" для перехода к форме создания заявки' \
         '\n\n' \
         'Hi! I am a bot computer network Baumanec. With the help of me, you can leave a request to the administrators ' \
         'of the hostel, one of them will contact you to help you connect to the Internet.' \
         'Click "Завяка" to go to the ticket creation form'

bay_msg = 'Спасибо за обращение! Мы посмотрим заявку и свяжемся с тобой в телеграмме.' \
          '\n\n' \
          'Thank you for contacting us! We will look at the ticket and contact you in a telegram'

cant_make_a_ticket = 'Что-то у нашего ботика сломалось( Пожалуйста, обратись к @alpoluyanov'\
                     '\n\n'\
                     'Something wrong, please contact @alpoluyanov'

particial_ticket = 'Кажется, заявка заполнена не до конца. Давай ещё раз пройдёмся по всем пунктам.'\
                   '\n\n'\
                   'It seems that the ticket is not fully completed. Let`s go through all the points again.'

from enum import Enum

token = "1234567:ABCxyz"
db_file = "database.vdb"


class States(Enum):
    """
    Мы используем БД Vedis, в которой хранимые значения всегда строки,
    поэтому и тут будем использовать тоже строки (str)
    """
    S_START = "0"  # Начало нового диалога
    S_ENTER_HOSTEL = "1"
    S_ENTER_ROOM = "2"
    S_ENTER_TROUBLE = "3"
