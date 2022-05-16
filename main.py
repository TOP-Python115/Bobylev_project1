# imports
import configparser

# global variables

FIELD = [[' '] * 3 for _ in range(3)]


# functions
# описания функций обязательны!
def field():
    # хорошее поле получилось
    global FIELD
    frame_h = "+———+———+———+"
    for row in FIELD:
        print(frame_h)
        print(f"| {row[0]} | {row[1]} | {row[2]} |")
    print(frame_h)
    pass


# ini file reading

# описания функций обязательны!
def print_menu(menu="main"):
    if menu == "main":
        print("1 - один игрок")
        print("2 - два игрока")


# описания функций обязательны!
def load(player_name) -> dict:
    cp = configparser.ConfigParser()
    res = {player_name: {}}
    try:
        cp.read("data.ini")
        for key in cp[player_name]:
            res[player_name][key] = cp[player_name][key]
    except:
        res = {}
    return res


# описания функций обязательны!
def save(player_name: str, player_stats: dict):
    cp = configparser.ConfigParser()
    cp[player_name] = player_stats
    with open("data.ini", "a") as f:
        cp.write(f)


# begin
while True:
    # я бы начал со справки: описать и себе и пользователю: что ты пользователю показать и что, от него получить
    print_menu()
    command = input()

    if command in ('quit', 'выход'):
        # Обработка завершения работы приложения
        break
    # используй комментарии! описывай, что делаешь
    elif command == "1":
        player_name = input("Ввведите имя игрока: ")
        if not load(player_name):
            save(player_name, {"wins": 0, "loses": 0, "draws": 0})
        else:
            player_stats = load(player_name)
            print(f"Статистика игрока {player_name}:\n"
                  f"Побед - {player_stats[player_name]['wins']}\n"
                  f"Поражений - {player_stats[player_name]['loses']}\n"
                  f"Ничьих - {player_stats[player_name]['draws']}")

# configparser работаем со словарём


# commit messages должны быть более информативные
# также, лучше больше коммитов, чем меньше
