import matplotlib.pyplot as plt


def graphs(input_filename):
    """
    Строит графики модуля скорости спутника от времени, расстояния до звезды от времени и модуля скорости
    от расстояния до звезды по данным из файла.
    Строчки файла должны быть определённого формата:
    <физическое время> <расстояние до Солнца> <модуль скорости>
    Параметры:
    input_filename: string - название файла для считывания данных
    """
    # Массивы, в которых будут храниться данные для построения графиков
    t = []
    v = []
    r = []

    with open(input_filename, 'r') as inp_file:
        for line in inp_file:
            if line != '':
                s = line.rstrip()
                s = s.split(' ')
                t.append(float(s[0]))
                r.append(float(s[1]))
                v.append(float(s[2]))

    # Отрисовка трёх графиков

    sp = plt.subplot(311)
    plt.plot(t, v, label='$\mid V \mid (t)$')
    plt.legend(loc='best', fontsize=10)
    plt.grid(True)

    sp = plt.subplot(312)
    plt.plot(r, v, label="$\mid V \mid (R)$")
    plt.legend(loc='best', fontsize=10)
    plt.grid(True)

    sp = plt.subplot(313)
    plt.plot(t, r, label="$\mid R \mid (t)$")
    plt.legend(loc='best', fontsize=10)
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    print("This module is not for direct call!")
