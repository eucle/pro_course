from string import ascii_lowercase as alow, ascii_uppercase as au, ascii_letters as al


def verification(login, password, success, failure):
    failure_msg = 0
    messages = {1: 'в пароле нет ни одной буквы',
                2: 'в пароле нет ни одной заглавной буквы',
                3: 'в пароле нет ни одной строчной буквы',
                4: 'в пароле нет ни одной цифры'}

    if not any(map(lambda x: x in al, password)):
        failure_msg = 1
    elif not any(map(lambda x: x in au, password)):
        failure_msg = 2
    elif not any(map(lambda x: x in alow, password)):
        failure_msg = 3
    elif not any(map(str.isdigit, password)):
        failure_msg = 4

    if failure_msg:
        failure(login, messages[failure_msg])
    else:
        success(login)
