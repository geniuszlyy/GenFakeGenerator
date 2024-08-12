from faker import Faker 
import logging 
import json 
from termcolor import colored 
from colorama import Fore, Style, init 

# Инициализация colorama
init(autoreset=True)

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Создание генератора фейковых данных
faker_instance = Faker('ru_RU')

# Функция для генерации и вывода различных фейковых данных
def generate_fake_data(data_type, count=1):
    data_list = []
    for _ in range(count):
        data = None
        if data_type == "name":
            data = faker_instance.name()
        elif data_type == "sentence":
            data = faker_instance.sentence()
        elif data_type == "address":
            data = faker_instance.address()
        elif data_type == "phone_number":
            data = faker_instance.phone_number()
        elif data_type == "coordinates":
            data = {
                "longitude": str(faker_instance.longitude()),
                "latitude": str(faker_instance.latitude())
            }
        elif data_type == "email":
            data = faker_instance.email()
        elif data_type == "job":
            data = faker_instance.job()
        elif data_type == "password":
            data = faker_instance.password(length=16, special_chars=True, digits=True, upper_case=True, lower_case=True)
        elif data_type == "color":
            data = faker_instance.rgb_css_color()
        elif data_type == "uri":
            data = faker_instance.uri()
        elif data_type == "text":
            data = faker_instance.text()
        elif data_type == "all":
            data = {
                "name": faker_instance.name(),
                "sentence": faker_instance.sentence(),
                "address": faker_instance.address(),
                "phone_number": faker_instance.phone_number(),
                "coordinates": {
                    "longitude": str(faker_instance.longitude()),
                    "latitude": str(faker_instance.latitude())
                },
                "email": faker_instance.email(),
                "job": faker_instance.job(),
                "password": faker_instance.password(length=16, special_chars=True, digits=True, upper_case=True, lower_case=True),
                "color": faker_instance.rgb_css_color(),
                "uri": faker_instance.uri(),
                "text": faker_instance.text()
            }
        if data is not None:
            data_list.append(data)
    return data_list

# Функция для сохранения данных в файл
def save_data_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    logging.info(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenFakeGenerator {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Данные сохранены в файл {Fore.LIGHTGREEN_EX}{filename}")

# Основной блок программы
if __name__ == "__main__":
    logo = """
   _____            ______    _         _____                           _             
  / ____|          |  ____|  | |       / ____|                         | |            
 | |  __  ___ _ __ | |__ __ _| | _____| |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | | |_ |/ _ \ '_ \|  __/ _` | |/ / _ \ | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |__| |  __/ | | | | | (_| |   <  __/ |__| |  __/ | | |  __/ | | (_| | || (_) | |   
  \_____|\___|_| |_|_|  \__,_|_|\_\___|\_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                      
                                                                                      
    """
    print(colored(logo, "red"))

    while True:
        print("\nВыберите тип данных для генерации:")
        print(colored("╔══════════════════════════════════════════════════╗", "cyan"))
        print(colored("║  1. Имя                                          ║", "cyan"))
        print(colored("║  2. Предложение                                  ║", "cyan"))
        print(colored("║  3. Адрес                                        ║", "cyan"))
        print(colored("║  4. Номер телефона                               ║", "cyan"))
        print(colored("║  5. Координаты                                   ║", "cyan"))
        print(colored("║  6. Почта                                        ║", "cyan"))
        print(colored("║  7. Профессия                                    ║", "cyan"))
        print(colored("║  8. Пароль                                       ║", "cyan"))
        print(colored("║  9. Цвет                                         ║", "cyan"))
        print(colored("║ 10. Ссылка                                       ║", "cyan"))
        print(colored("║ 11. Текст                                        ║", "cyan"))
        print(colored("║ 12. Всё вместе                                   ║", "cyan"))
        print(colored("║  0. Выход                                        ║", "cyan"))
        print(colored("╚══════════════════════════════════════════════════╝", "cyan"))

        choice = input(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenFakeGenerator {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Введите номер: {Fore.LIGHTGREEN_EX}")

        if choice == "0":
            break

        data_types = {
            "1": "name",
            "2": "sentence",
            "3": "address",
            "4": "phone_number",
            "5": "coordinates",
            "6": "email",
            "7": "job",
            "8": "password",
            "9": "color",
            "10": "uri",
            "11": "text",
            "12": "all"
        }

        data_type = data_types.get(choice)
        if data_type:
            count = int(input(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenFakeGenerator {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Введите количество для генерации: {Fore.LIGHTGREEN_EX}"))
            generated_data = generate_fake_data(data_type, count)
            if generated_data:
                filename = f"{data_type}.json" if data_type != "all" else "all_data.json"
                save_data_to_file(generated_data, filename)
        else:
            logging.error(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenFakeGenerator {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» {Fore.LIGHTYELLOW_EX}Неверный ввод, попробуйте снова.")
