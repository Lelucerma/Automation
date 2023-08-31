def open_file():
    # 打开数据文件
    # file_path = "D:\\2 code\\automation\\data\\230723\\230723\\"
    file1 = './data/230801/pump4_200.txt'
    a = open(file1, "r+")
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



a, m, p = open_file()
print(a)
print(m)
print(p)