import matplotlib.pyplot as plt
import numpy as np
import os


def open_file(file_name):
    # 打开数据文件
    # file_path = "D:\\2 code\\automation\\data\\230723\\230723\\"
    # file1 = file_name
    a = open(file_name, "r+")
    data = a.readlines()
    num_lenth = len(data)
    y1,y2 = [], []
    for line in data:
        ever_line = line.strip()
        m1, m2 = tran_num(ever_line)
        y1.append(m1)
        y2.append(m2)
    a.close()
    return num_lenth, y1, y2

def tran_num(ever_line):
    ever_data = ever_line.split("'")[1:]
    # print(ever_data)
    ever_data1 = ever_data[0]
    ever_data1 = ever_data1.split("K")
    ever_data2 = ever_data[2]
    ever_data2 = ever_data2.split("K")
    return float(ever_data1[0]), float(ever_data2[0])


# 准备绘制数据
def plt_picture(file_path, file_name):

    file_name = str(file_name.split('.txt')[0])
    file1 = file_path + "\\" + file_name + '.txt'
    a = open(file_name, "r+")
    data = a.readlines()
    ever_lines = []
    i = 0
    col = ['r', 'b', 'g', 'y', 'm', 'c']
    for line in data:
        ever_lines.append(line.strip())
    for ever_data in ever_lines:
        xi = np.arange(98)
        yi = ever_data
        # "r" 表示红色，marksize用来设置'D'菱形的大小
        plt.plot(xi, yi, c=col[i], label="pressure")
    # 绘制坐标轴标签
    plt.xlabel("t/s", labelpad=-12, x=1.02)
    plt.ylabel("p/Kpa", labelpad=-9, y=1.1)

    plt_name = file_name[5:-4] + " pressure change"
    plt.title(plt_name, x=0.5, y=1.05)
    # 显示图例
    plt.legend(loc="upper right")
    # 保存图片
    # picture_path = "D:\\2 code\\automation\\data\\picture\\"
    picture_name = file_name + ".png"
    # print(picture_name)
    plt.savefig(picture_name)
    plt.show()

    # 调用 text()在图像上绘制注释文本
    # x1、y1表示文本所处坐标位置，ha参数控制水平对齐方式, va控制垂直对齐方式，str(y1)表示要绘制的文本
    # for x1, y1 in zip(x, y):
    #     plt.text(x1, y1, str(y1), ha='center', va='bottom', fontsize=10)


def plt_pictures(file_path, file_name, m=8):

    col = ['r', 'b']
    file_name = str(file_name.split('.txt')[0])
    file1 = file_path + "\\" + file_name + '.txt'
    xi, y1, y2 = open_file(file1)
    xi = np.arange(xi)

    # col = (np.random.random(), np.random.random(), np.random.random())
    # "r" 表示红色，marksize用来设置'D'菱形的大小
    plt.plot(xi,
                y1,
                'r',
                marker='x',
                label=f"3th",
                markersize=3)
    plt.plot(xi,
                y2,
                'b',
                marker='x',
                label=f"4th",
                markersize=3)
    # col = (np.random.random(), np.random.random(), np.random.random())
    # "r" 表示红色，marksize用来设置'D'菱形的大小
    # 绘制坐标轴标签
    plt.xlabel("t/s", labelpad=-12, x=1.02)
    plt.ylabel("p/Kpa", labelpad=-9, y=1.1)

    plt_name = file_name + " pressure change"
    plt.title(plt_name, x=0.5, y=1.05)
    # 显示图例
    plt.legend(loc="upper right")
    # 保存图片
    picture_path = path + '\\' + "picture"
    floder = os.path.exists(picture_path)
    if not floder:
        os.mkdir(picture_path)
    picture_name = picture_path + '\\' + picture_name + '.png'
    print(picture_name)
    plt.savefig(picture_name)
    plt.show()

    # 调用 text()在图像上绘制注释文本
    # x1、y1表示文本所处坐标位置，ha参数控制水平对齐方式, va控制垂直对齐方式，str(y1)表示要绘制的文本
    # for x1, y1 in zip(x, y):
    #     plt.text(x1, y1, str(y1), ha='center', va='bottom', fontsize=10)

def floder(path):
    # path = 'D:\\2 code\\Automation\data\\230816'

    files = os.listdir(path)
    s = []
    for file in files:
        if not os.path.isdir(file):
            s.append(file)
    return s


# def main():
#     # file_name1 = ['tran_wang_deprotection.txt',
#                       'tran_wang_deprotection2.txt']
#     # file_name2 = ['tran_gly1_couple.txt', 'tran_gly1_deprotection.txt']
#     # file_name3 = ['tran_gly2_couple.txt', 'tran_gly2_deprotection.txt']
#     # file_name4 = ['tran_phe_couple.txt', 'tran_phe_deprotection.txt']
#     # file_name5 = ['tran_tyr_couple.txt']
#     # plt_pictures(file_name1, 9)
#     # plt_pictures(file_name2, 9)
#     # plt_pictures(file_name3, 9)
#     # plt_pictures(file_name4)
#     # plt_pictures(file_name5)

path = 'D:\\0 厦门大学\\10 实验\数据\\20240724'
files = floder(path)
file_name = '240724pheouhe1.txt'
plt_picture(path, file_name)
# for file_name in files:
#     plt_pictures(path, file_name)


# main()
