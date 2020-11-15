import matplotlib.pyplot as plt
import numpy as np


def graphs(input_filename):
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
    sp = plt.subplot(311)
    plt.plot(t, v)
    plt.title("$\mid V \mid (t)$")
    plt.grid(True)

    sp = plt.subplot(312)
    plt.plot(r, v)
    plt.title("$\mid V \mid (R)$")
    plt.grid(True)

    sp = plt.subplot(313)
    plt.plot(t, r)
    plt.title("$\mid R \mid (t)$")
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    print("This module is not for direct call!")