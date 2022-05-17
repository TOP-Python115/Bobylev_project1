# imports
from configparser import ConfigParser

# global variables

FIELD = [[' '] * 3 for _ in range(3)]
PLAYERS = {}
SAVES = {}


# functions
def field() -> None:
    """Вывод на экран игрового поля с ходами"""
    # хорошее поле получилось
    global FIELD
    frame_h = "+———+———+———+"
    for row in FIELD:
        print(frame_h)
        print(f"| {row[0]} | {row[1]} | {row[2]} |")
    print(frame_h)


def print_menu(menu="main") -> None:
    """Вывод на экран игровых меню"""
    if menu == "main":
        print("1 - один игрок")
        print("2 - два игрока")


def show_help() -> None:
    """Вывод на экран справочной информации"""
    # TODO реализовать функцию
    pass


def read() -> bool:
    """Загрузка сохранённых данных из файла в глобальные переменные"""
    global PLAYERS, SAVES
    config = ConfigParser()
    if config.read("data.ini", encoding="utf-8"):
        PLAYERS = {name.title(): [int(n) for n in score.split(',')]
                   for name, score in config["Scores"].items()}
        SAVES = {tuple(name.split(';')):
                     [[' ' if c == '-' else c for c in field[i:i + 3]]]
                 for i in range(0, 9, 3) for name, field in config["Saves"].items()}
        return True if config["General"]["first"] == "yes" else False
    else:
        raise FileNotFoundError


def save() -> None:
    """Сохранение данных из глобальных переменных в файл"""
    global PLAYERS, SAVES
    config = ConfigParser()
    config["Scores"] = {name: ','.join([str(x) for x in score]) for name, score in PLAYERS.items()}
    config["Saves"] = {';'.join(name):
                           ''.join(['-' if cell == ' ' else cell for row in field for cell in row])
                       for name, field in SAVES.items()}
    config["General"]["first"] = "no"
    with open("data.ini", 'w', encoding="utf-8") as f:
        config.write(f)


if read():
    show_help()

# Основной цикл игры
while True:
    # я бы начал со справки: описать и себе и пользователю: что ты пользователю показать и что, от него получить
    print_menu()
    command = input()

    if command in ('quit', 'выход'):
        # Обработка завершения работы приложения
        break
