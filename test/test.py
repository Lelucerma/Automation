import matplotlib.pyplot as plt
import numpy as np


def analysis():
    file_test = open("test/2.txt", 'r')
    datas = []
    data = file_test.read().split("<")
    data = data[1].split(">")
    data = data[1].split(" ")
    for i in data:
        datas.append(float(i))
    xi = np.arange(len(datas))
    plt.plot(xi, datas)
    plt.show()
    # print(data)


def s():
    file_test = open("data\\test002@(UV-ch1-214) .txt", 'r')
    data = file_test.readlines()
    xi, yi = [], []
    for i in data:
        i = i.split("\t")
        xi.append(float(i[0]))
        i[1] = i[1].split("\n")
        yi.append(float(i[1][0]))
    plt.plot(xi, yi)
    plt.show()


analysis()
s()
