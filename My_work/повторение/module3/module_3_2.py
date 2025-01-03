def is_valid_send(sender):
    return '@' in sender and sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net')


def is_valid_recip(recipient):
    return '@' in recipient and recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net')


def send_email(message, recipient, sender="university.help@gmail.com"):
    sender_e = sender

    if sender == recipient:
        print(f'Нельзя отправить письмо самому себе!')

    elif not is_valid_send(sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    elif not is_valid_recip(recipient):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    elif sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


    elif sender_e is sender:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
