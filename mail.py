COLOR_CODE = {
    "RESET": "\033[0m",  
    "GREEN": "\033[32m",     
    "BOLD": "\033[01m",
    "RED": "\033[31m"  
}

def get_mail(database_file, search_value):
    found = False

    with open(database_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')  
        if len(data) >= 21:  # Изменил проверку здесь
            email = data[8]
            if search_value in email:
                user_id = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                middle_name = data[4]
                birthday = data[5]
                gender = data[6]
                phone = data[7]
                role = data[9]
                class_name = data[13]
                address = data[19]
                country = data[16]
                citizenship = data[15]
                region = data[17]  
                municipal_education = data[18]  
                institution_name = data[20]  

                print(f'''{COLOR_CODE["PINK"]}
╔══════                                               ══════╗
║                                                           ║
                [+] ID пользователя: {user_id}
                [+] Дата регистрации: {registration_date}
                [+] Фамилия: {last_name}
                [+] Имя: {first_name}
                [+] Отчество: {middle_name}
                [+] Дата рождения: {birthday}
                [+] Пол: {gender}
                [+] Телефон: {phone}
                [+] Почта: {email}
                [+] Роль: {role}
                [+] Класс: {class_name}
                [+] Адрес: {address}
                [+] Страна: {country}
                [+] Гражданство: {citizenship}
                [+] Регион: {region}
                [+] Муниципальное образование: {municipal_education}
                [+] Наименование учреждения: {institution_name}  
║                                                           ║
╚══════                                               ══════╝
                     
                      ''')
                found = True

    if not found:
        print(f'{COLOR_CODE["GREEN"]}[ERROR] Я ничего не нашел в базе')
        get_yandex_eda_number(database_file, search_value)  # вызов второй функции

def get_yandex_eda_number(database_file, search_value):
    found = False
    with open(database_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    search_value = search_value.strip().lower()  # Приводим к нижнему регистру и убираем пробелы

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 5:
            phone = data[0].strip().lower()
            if search_value in phone:
                first_name = data[1]
                full_name = data[2]
                email = data[3]
                address_info = data[4].split(',')

                address_city = address_info[0]
                address_street = address_info[1]
                address_house = address_info[2]
                address_entrance = address_info[3]

                print(f'''{COLOR_CODE["GREEN"]}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]}Телефон: {phone}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]}Имя: {first_name}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]}Полное имя: {full_name}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]}Электронная почта: {email}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]}Город: {address_city}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]}Улица: {address_street}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]}Дом: {address_house}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]}Подъезд: {address_entrance}
                ''')
                found = True

    if not found:
        print(f'{COLOR_CODE["RED"]}[ERROR] {COLOR_CODE["GREEN"]}Ничего не найдено в базе данных по номеру телефона :(.{COLOR_CODE["RESET"]}')

