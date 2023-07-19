class test():
    def trans(self,data):
        self.data = data
        # 除去二进制数中的开头
        self.bin = bin(0)[:2]
        # print(self.bin)
        # 转换成二进制的数值
        self.datas = bin(self.data)
        # 除去二进制数中的开头
        self.datas = self.datas[2:]
        # print(self.datas)
        # print(len(self.datas))
        if len(self.datas) < 8:
            self.datah = [0]
            self.datal = [int(self.bin + self.datas, 2)]
        elif (len(self.datas) > 8) and (len(self.datas) < 16):
            self.l = (len(self.datas) - 8)
            # print(self.l)
            self.datah = [int(self.bin + self.datas[:-8], 2)]
            self.datal = [int(self.bin + self.datas[8:], 2)]
        else:
            error = 1  # 报错
        return self.datah, self.datal

# a = test()
# s1,s2 = a.trans(12345)
# print(s1,s2)


data = hex(12345)
datal = [int(data[2:4],16), int(data[4:6],16)]
print(datal)