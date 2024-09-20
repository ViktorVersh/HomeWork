def is_valid_email(recipient):
    return '@' in recipient and (recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net'))


def is_valid_email(sender):
    return '@' in sender and (sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'))


def send_email(message, recipient, sender="university.help@gmail.com"):
    sender_e = sender
    if recipient == sender:
        result_3 = "Нельзя отправить письмо самому себе!"
        print(result_3)
    elif not is_valid_email(recipient):
        result = f'"Невозможно отправить письмо с адреса {sender} на адрес {recipient}"'
        print(result)
    elif not is_valid_email(sender):
        result_2 = f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}"
        print(result_2)
    elif sender != "university.help@gmail.com":
        result_5 = f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}."
        print(result_5)
    elif sender_e is sender:
        result_4 = f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}."
        print(result_4)
    else:
        print()


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
