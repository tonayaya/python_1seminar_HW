def get_info():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_number = input('Введите номер телефона: ')
    info.append(phone_number)
    discription = input('Введите описание: ')
    info.append(discription)
    return info