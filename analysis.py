import matplotlib.pyplot as plt
import numpy as np


def opne_file(file_name):
    # 打开数据文件
    # file_path = "D:\\2 code\\automation\\data\\230723\\230723\\"
    file1 = file_name
    a = open(file1, "r+")
    data = a.readlines()
    num_lenth = len(data)
    y = []
    for line in data:
        eyer_line = line.strip()
        eyer_data = eyer_line.split(":")[1:]
        eyer_data = eyer_data[0].split("K")[:1]
        y.append(float(eyer_data[0]))
    a.close()
    return num_lenth, y


# 准备绘制数据
def plt_picture(file_name):

    xi, yi = opne_file(file_name)
    xi = np.arange(xi)
    # "r" 表示红色，marksize用来设置'D'菱形的大小
    plt.plot(xi, yi, "r", label="pressure")
    # 绘制坐标轴标签
    plt.xlabel("t/s", labelpad=-12, x=1.02)
    plt.ylabel("p/Kpa", labelpad=-9, y=1.1)

    plt_name = file_name[5:-4] + " pressure change"
    plt.title(plt_name, x=0.5, y=1.05)
    # 显示图例
    plt.legend(loc="upper right")
    # 保存图片
    picture_path = "D:\\2 code\\automation\\data\\picture\\"
    picture_name = file_name[5:-4] + ".png"
    picture_name = picture_path + picture_name
    # print(picture_name)
    plt.savefig(picture_name)
    plt.show()

    # 调用 text()在图像上绘制注释文本
    # x1、y1表示文本所处坐标位置，ha参数控制水平对齐方式, va控制垂直对齐方式，str(y1)表示要绘制的文本
    # for x1, y1 in zip(x, y):
    #     plt.text(x1, y1, str(y1), ha='center', va='bottom', fontsize=10)


def plt_pictures(file_name, m=8):

    col = ['r', 'b']

    for num, ever_name in enumerate(file_name):
        xi, yi = opne_file(ever_name)
        xi = np.arange(xi)

        # col = (np.random.random(), np.random.random(), np.random.random())
        # "r" 表示红色，marksize用来设置'D'菱形的大小
        plt.plot(xi,
                 yi,
                 c=col[num],
                 marker='x',
                 label=f"{ever_name[5:-4]}",
                 markersize=3)
        # col = (np.random.random(), np.random.random(), np.random.random())
        # "r" 表示红色，marksize用来设置'D'菱形的大小
    # 绘制坐标轴标签
    plt.xlabel("t/s", labelpad=-12, x=1.02)
    plt.ylabel("p/Kpa", labelpad=-9, y=1.1)

    plt_name = file_name[0][5:-4] + " pressure change"
    plt.title(plt_name, x=0.5, y=1.05)
    # 显示图例
    plt.legend(loc="upper right")
    # 保存图片
    picture_path = "D:\\2 code\\automation\\data\\picture\\"
    picture_name = file_name[0][5:m] + ".png"
    picture_name = picture_path + picture_name
    # print(picture_name)
    plt.savefig(picture_name)
    plt.show()

    # 调用 text()在图像上绘制注释文本
    # x1、y1表示文本所处坐标位置，ha参数控制水平对齐方式, va控制垂直对齐方式，str(y1)表示要绘制的文本
    # for x1, y1 in zip(x, y):
    #     plt.text(x1, y1, str(y1), ha='center', va='bottom', fontsize=10)


# def main():
#     # file_name1 = ['tran_wang_deprotection.txt', 'tran_wang_deprotection2.txt']
#     # file_name2 = ['tran_gly1_couple.txt', 'tran_gly1_deprotection.txt']
#     # file_name3 = ['tran_gly2_couple.txt', 'tran_gly2_deprotection.txt']
#     # file_name4 = ['tran_phe_couple.txt', 'tran_phe_deprotection.txt']
#     # file_name5 = ['tran_tyr_couple.txt']
#     # plt_pictures(file_name1, 9)
#     # plt_pictures(file_name2, 9)
#     # plt_pictures(file_name3, 9)
#     # plt_pictures(file_name4)
#     # plt_pictures(file_name5)
#     file_name = 'tran_wang_deprotection.txt'
#     plt_picture(file_name)


# main()
