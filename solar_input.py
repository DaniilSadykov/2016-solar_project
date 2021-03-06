# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Считывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """

    s = line.strip()

    s = s.split(' ')

    star.R = float(s[1])

    star.color = s[2]

    star.m = float(s[3])

    star.x = float(s[4])

    star.y = float(s[5])

    star.Vx = float(s[6])

    star.Vy = float(s[7])


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    s = line.strip()

    s = s.split(' ')

    planet.R = float(s[1])

    planet.color = s[2]

    planet.m = float(s[3])

    planet.x = float(s[4])

    planet.y = float(s[5])

    planet.Vx = float(s[6])

    planet.Vy = float(s[7])


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(obj.type, obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy, file=out_file)


def save_stats_to_file(output_filename, object, t):
    """
    Сохраняет статистику для выведения графиков о движении спутника в файл.
    Строки имеют следующий формат:
    <физическое время> <расстояние до Солнца> <модуль скорости>
    """
    with open(output_filename, 'a') as out_file:
        distance_from_sun = (object.x**2 + object.y**2) ** 0.5
        absolute_velocity = (object.Vx**2 + object.Vy**2) ** 0.5
        print(t, distance_from_sun, absolute_velocity, file=out_file)


if __name__ == "__main__":
    print("This module is not for direct call!")
