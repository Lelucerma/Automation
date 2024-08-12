'''
Author: wang w1838978548@126.com
Date: 2024-01-08 15:35:26
LastEditors: wang w1838978548@126.com
LastEditTime: 2024-07-29 16:09:15
FilePath: \practice\test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import matplotlib.pyplot as plt
import os
import numpy as np
from scipy import integrate
from scipy.signal import find_peaks, peak_widths

# pathname = ".\\data\\20240724"
pathname = "D:\\0 厦门大学\\10 实验\\数据\\20240724"
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
        """
        对每个文件里面的数据进行处理，得到一个列表，第一项是x轴的数据
        第二项是y轴的数据
        :param filename: 需要进行处理的文件名
        :return: datas: 这是一个列表的数据
        """
        f = filename
        file_uv = open(f, 'r')
        datas = []
        data = file_uv.readlines()
        xi, yi, k = [], [], []
        # 对于每个文件中的数据进行处理
        for ever_line in data:
            # 对每行的数据进行梳理
            temp = ever_line.split('\t')
            # 将每行的横坐标数据和纵坐标数据进行分离
            temp[1] = temp[1].split('\n')
            x = float(temp[0])
            # print(x)
            y = float(temp[1][0])
            # 处理掉无法使用的数据
            if x > 27 and x < 33:
                pass
            elif x > 40:
                pass
            else:
                xi.append(x)
                yi.append(y)
            # 使用全部数据
            # xi.append(x)
            # yi.append(y)
        # 将数据放入到一个列表中
        datas.append(xi)
        datas.append(yi)
        return datas

    def dataProcess(self, data):
        """
        对处理好的数据寻找相应的峰，并返回相应的峰高和峰宽数据
        :param data: 这是一个列表，已经经过处理过的数据，
        :return: widths: 这是一个列表，里面是峰宽的数据，第一个数据是峰的宽度，
                        第二个是这个峰相较于基线的高度，第三个是峰的起始时间
                        第四个是峰的结束时间。
                peaks: 这是一个列表，里面包含里峰高的数据，第一个是最高峰对应的时间
                        第二个是峰的高度
                areas: 每个峰的峰面积的值
        """
        x_peaks, y_peaks = [], []
        width, widths = [], []
        areas = []
        peaks1, _ = find_peaks(data[1], height=100, distance=100)
        width1 = peak_widths(data[1], peaks1, rel_height=1, wlen=1000)
        for i in range(4):
            if i == 0:
                for j in width1[i]:
                    width.append(j / 1000)
            elif i <= 1:
                for j in width1[i]:
                    width.append(j)
            else:
                for j in width1[i]:
                    width.append(data[0][int(j)])
            widths.append(width)
            width = []
        for i in peaks1:
            x_peaks.append(data[0][i])
            y_peaks.append(data[1][i])
        peaks = [x_peaks, y_peaks]
        for i in range(len(widths[2])):
            boundary = [widths[2][i], widths[3][i]]
            area = self.dataIntegrate(data[1], boundary)
            areas.append(area)
        return widths, peaks, areas

    def dataIntegrate(self, data, boundary):
        area = integrate.trapz(data, boundary)
        return area

    def draw_picture(self, data, filename, widths, peaks, areas):
        """
        画出相应的峰形并标出相应的出峰位置和时间。
        :param data: 处理之后的数据
        :param filename:文件名
        :param widths:峰款的数据
        :param peaks:峰高的数据
        :return:无
        """
        x_peaks, y_peaks = peaks[0], peaks[1]
        filename = filename.split("\\")
        fig = plt.figure(figsize=(20, 10))
        a1 = plt.subplot2grid((1, 6), (0, 0), colspan=4)
        a2 = plt.subplot2grid((1, 6), (0, 4), colspan=2)
        my_x_ticks = np.arange(0, int(max(data[0])) + 5, 1)
        for i in y_peaks:
            a1.text(x_peaks[y_peaks.index(i)], i + 80, f'{i}')
        a1.plot(x_peaks, y_peaks, 'x', color='r')
        a1.hlines(*widths[1:], color="r")
        a1.plot(data[0], data[1], color='black')
        a1.set_title(filename[-1][:-4])
        a1.set_ylabel("uv(mAu)")
        a1.set_xlabel("t(min)")
        a1.set_xticks(my_x_ticks)
        a2.plot(x_peaks, y_peaks, label='high')
        # a2.plot(x_peaks, areas, '--')
        a3 = a2.twinx()
        a3.plot(x_peaks, areas, color='#ffaa00', label='area')
        lines, labels = a2.get_legend_handles_labels()
        lines2, labels2 = a3.get_legend_handles_labels()
        a2.legend(lines + lines2, labels + labels2, loc='upper right')

        plt.show()


for file in fileFliter:
    all_ever = 0
    a = Data_ana()
    file1 = pathname + "\\" + file
    ever_data = a.data1(file1)
    widths, peaks, areas = a.dataProcess(ever_data)
    a.draw_picture(ever_data, file1, widths, peaks, areas)
