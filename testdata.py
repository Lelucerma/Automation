'''
Author: wang w1838978548@126.com
Date: 2024-01-08 15:35:26
LastEditors: wang w1838978548@126.com
LastEditTime: 2024-07-24 17:54:19
FilePath: \practice\test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import matplotlib.pyplot as plt
import os
import numpy as np
from scipy.signal import find_peaks, peak_widths

pathname = ".\\data\\20240724"
# pathname = "D:\\0 厦门大学\\10 实验\\荧光"
filenames = os.listdir(pathname)  # 获取该目录下所有的文件
fileFliter = []
filesave = filedata = pathname + "\\" + "alls.xls"
# 过滤掉后缀不为txt的文件
for filename in filenames:
    suffix = os.path.splitext(filename)[-1]
    if suffix == '.txt':
        fileFliter.append(filename)
areas = []


class Data_ana():
    def data1(self, filename):
        f = filename
        file_uv = open(f, 'r')
        datas = []
        data = file_uv.readlines()
        xi, yi, k = [], [], []
        # 对于每个文件中的数据进行处理
        for ever_line in data:
            temp = ever_line.split('\t')
            temp[1] = temp[1].split('\n')
            x = float(temp[0])
            # print(x)
            y = float(temp[1][0])
            # if x > 27 and x < 33:
            #     pass
            # elif x > 41:
            #     pass
            # else:
            #     xi.append(x)
            #     yi.append(y)
            xi.append(x)
            yi.append(y)
        datas.append(xi)
        datas.append(yi)
        return datas

    def data_analysis(self, data, x1, x2):
        xi = data[0]
        yi = data[1]
        x = 0.001
        start, stop = xi.index(x1), xi.index(x2)
        area = 0
        # print(xi[start], xi[stop])
        for num in range(start, stop):
            if yi[num] > 100:
                area += x * yi[num]
            else:
                pass
        return area

    def slop_Detection(self, y1, y2):
        x = 0.001
        k = (y2 - y1) / x
        return k

    # 进行斜率判断，将斜率变化较大地方的数据提取出来
    def slop_judgement(self, data):
        tempk0, tempk = 0, 0
        datax = data[0]
        datay = data[1]
        slop_start = []
        slop_stop = []
        for num, data in enumerate(datay):
            if num == 0:
                tempk = self.slop_Detection(data, datay[num + 1])
            else:
                tempk = self.slop_Detection(datay[num - 1], data)

            if -1000 < tempk and tempk < 1000:
                if tempk0 < -1000:
                    slop_stop.append(datax[num])
            elif 1000 < tempk:
                if -1000 < tempk0 and tempk0 < 1000:
                    slop_start.append(datax[num])
            tempk0 = tempk
        slop_start = self.dell(slop_start)
        slop_stop = self.dell(slop_stop)
        # print(slop_start, slop_stop)
        return slop_start, slop_stop

    # 对提取出来的峰的数据进行相应的判断
    def peak_judgement(self, slop_start, slop_stop):
        if slop_start[0] == 0.0:
            slop_start.pop(0)
        # print(slop_start)
        # print(slop_stop)
        slop_start_tran, slop_stop_tran = [], []
        x_start, x_stop = len(slop_stop), len(slop_start)
        m, i, j = 0, 0, 0
        while i < x_stop:
            if j == x_start -1 :
                if slop_start[j] < slop_stop[-1]:
                    slop_start_tran.append(slop_start[j])
                    slop_stop_tran.append(slop_stop[i])
                    break
            else:
                if slop_start[j] < slop_stop[i]:
                    if slop_start[j+1] > slop_stop[i]:
                        slop_start_tran.append(slop_start[m])
                        slop_stop_tran.append(slop_stop[i])
                        i += 1
                        j += 1
                        m = j
                    else:
                        m = j
                        j += 1
                else:
                    j += 1
        return slop_start_tran, slop_stop_tran

    # 去除相近的数据值
    def dell(self, origin_data):
        length = len(origin_data)
        tran_data=[]
        i = 0
        tran_data.append(origin_data[0])
        for j in origin_data:
            if i == len(origin_data) - 1:
                # print(i)
                break
            temp = origin_data[i + 1] - j
            if temp > 0.05:
                tran_data.append(origin_data[i+1])
            i += 1
        return tran_data

    def draw_picture(self, data, filename):
        plt.figure(num=1,figsize=(20,10))
        filename = filename.split("\\")
        y = data[1]
        # y = np.array(y)
        x = data[0]
        y2 = np.array(data[1])
        # cls = #55ffff
        peaks1, _ = find_peaks(y, height=100)
        # peaks2, _ = find_peaks(y2, height=100)
        width1 = peak_widths(y, peaks1, rel_height=1)
        # width2 = peak_widths(y2, peaks2, rel_height=1)
        plt.title(filename[-1][:-4])
        plt.ylabel("uv(mAu)")
        plt.xlabel("t(min)")
        xmax = int(max(x)) + 5 
        my_x_ticks = np.arange(0,xmax,1)
        plt.plot(x, y, color='#55aaffff')
        # plt.plot(peaks1, y[peaks1], "x")
        # plt.hlines(*width1[1:], color="C4")
        # plt.plot(y2)
        # plt.plot(peaks2, y2[peaks2], "+")
        # plt.hlines(*width2[1:], color="C3")
        # print(width)
        plt.xticks(my_x_ticks)
        plt.show()

for file in fileFliter:
    # slop_judgement()
    # print(file)
    all_ever = 0
    a = Data_ana()
    file1 = pathname + "\\" + file
    # print(file1)
    ever_data = a.data1(file1)
    # print(ever_data[1])
    # print(ever_data[1])
    # c, b = a.slop_judgement(ever_data)
    # m, n = a.peak_judgement(c, b)
    # print(m, n)
    # for i in range(len(m)):
    #     ever_area = a.data_analysis(ever_data, m[i], n[i])
    #     all_ever += ever_area
    #     print("%f: %.3f" % (m[i], ever_area))
    # # print("%.3f"%all_ever)

    a.draw_picture(ever_data, file1)



# print(dell([0.791, 1.218, 1.925, 2.011, 3.31, 3.345, 3.401, 4.104, 4.107, 4.109, 4.8, 4.803]))
