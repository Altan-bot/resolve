def send_email(message: str, recipint: str, sender="university.help@gmail.com"):
    valid_sender = sender.endswith((".com",".ru",".net")) and "@" in sender
    valid_recipient = recipint.endswith((".com",".ru",".net")) and "@" in  recipint

    if not valid_sender or not valid_recipient:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipint}")

    elif sender == recipint:
        print("Нельзя отправить письмо самому себе!")

    elif valid_recipient and valid_sender:
        if sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipint}.")
        else:
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлино с адреса {sender} на адрес {recipint}.")


send_email(message='Это сообщение для проверки связи', recipint= 'vasyok1337@gmail.com')
send_email(message='Вы видите это сообщение как лучший студент курса!', recipint= 'urban.fan@mail.ru',sender='urban.info@gmail.com')
send_email(message='Пожалуйстаб, исправьте задание', recipint= 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email(message='Напоминаю самому себе о вебинаре',recipint='urban.teacher@mail.ru',sender='urban.teacher@mail.ru')