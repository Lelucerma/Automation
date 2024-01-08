import matplotlib.pyplot as plt
import numpy as np
import os
import xlwt

pathname = "D:\\0 厦门大学\\10 实验\数据\\231217"
filenames = os.listdir(pathname)  # 获取该目录下所有的文件
fileFliter = []
filesave = filedata = pathname + "\\" + "alls.xls"
# 过滤掉后缀不为txt的文件
for filename in filenames:
    suffix = os.path.splitext(filename)[-1]
    if suffix == '.txt':
        fileFliter.append(filename)
areas = []
workbook = xlwt.Workbook(encoding="ascii")
worksheet = workbook.add_sheet("shhet1")

def draw_picture(fileFliter):
    row = 0
    column = 0
    # 每个文件进行画图
    for filename in fileFliter:
        # filename = "231214phe@(UV-ch1-310) "
        filedata = pathname + "\\" + filename
        file_picture = pathname + "\\" + filename + ".png"

        file_uv = open(filedata, 'r', encoding='gbk')

        data = file_uv.readlines()
        xi, yi = [], []

        # 对于每个文件中的数据进行处理
        for ever_line in data:
            temp = ever_line.split('\t')
            temp[1] = temp[1].split('\n')
            x = float(temp[0])
            y = float(temp[1][0])
            xi.append(x)
            yi.append(y)
            worksheet.write(row, column, y)
            row += 1
        row = 0
        column += 1

        areas.append(data_analysis(yi))

        # plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.title(filename[:-4])
        plt.ylabel("uv(mAu)")
        plt.xlabel("t(s)")

        plt.plot(xi, yi)
        plt.show()

        file_uv.close()
        # 将所有的数据存储到一个文件里面
    # workbook.save(filesave)
    # print(areas)

def data_analysis(datay):
    x = 0.001
    area = 0
    for y in datay:
        if y > 100:
            area += x * y
        else:
            pass

    return area

def slop_Detection(y1, y2):
    x = 0.001
    if y1 < 0:
        y1 = np.abs(y1)
    if y2 < 0:
        y2 = np.abs(y2)
    k = (y2 - y1) / x
    return k


draw_picture(fileFliter)


def peak_judgement():
    f = "D:\\0 厦门大学\\10 实验\\数据\\231217\\tyr0.2-0.35@(UV-ch1-310) .txt"
    file_uv = open(f, 'r')

    data = file_uv.readlines()
    xi, yi, k = [], [], []

    # 对于每个文件中的数据进行处理
    for ever_line in data:
        temp = ever_line.split('\t')
        temp[1] = temp[1].split('\n')
        x = float(temp[0])
        y = float(temp[1][0])
        xi.append(x)
        yi.append(y)

    tempk0, tempk = 0, 0
    datax = xi
    datay = yi
    slop_start = []
    slop_stop = []
    for num, data in enumerate(datay):
        if num == 0:
            tempk = slop_Detection(data, datay[num + 1])
        else:
            tempk = slop_Detection(datay[num - 1], data)
        # worksheet.write(num, 0, datax[num])
        # worksheet.write(num, 1, datay[num])
        # worksheet.write(num, 2, tempk)
        # k.append(tempk)

        if -1000 < tempk and tempk < 1000:
            if tempk0 < -1000:
                print(datax[num],tempk,tempk0)
        # elif -3000 < tempk or tempk < -100 or 100 < tempk or tempk < 3000:
        #     continue
        # else:
        #     if tempk0 < -3000 or 3000 < tempk0:
        #         continue
        #     else:
        #         slop_start.append(num)
        tempk0 = tempk
    # print(xi,yi,k)
    # workbook.save("D:\\0 厦门大学\\10 实验\\数据\\231217\\tyr0.2-0.35@(UV-ch1-310) .xls")
    return slop_start,slop_stop

peak_judgement()
# print(peak_judgement())

