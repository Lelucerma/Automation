class s():  
    def reaction_unit5_time(self,
                      slave_add1=1,
                      speed=None,
                      volume=None,
                      next_unit=None,
                      speed_before=0):
        """"
        计算各个听写的时间

        Args:

            * slave_add1 第一个泵
            * slave_add2 第二个泵
            * speed 四个泵的运行速度
            * volume 两个反应物的投料量

        """
        if speed is None:
            speed = []
        if volume is None:
            volume = []
        if slave_add1 == 0:
            pass
        else:
            self.slave_add1, self.slave_add2 = slave_add1, slave_add1+1
            self.slave_add3, self.slave_add4 = slave_add1+2, slave_add1+3
            self.slave_add5 = slave_add1 + 4
        if not speed:
            pass
        else:
            self.speed1, self.speed2 = speed[0], speed[1]
            self.speed3, self.speed4 = speed[2], speed[3]
            self.speed5 = speed[4]
        if not volume:
            pass
        else:
            self.volume1, self.volume4 = volume[0], volume[1]

        # 计算各个泵需要的运行时间,不同的进料体积需要不同的进料速度
        self.volume5_time()

        # 进行各个时间的计算程序
        self.run_time()

        # 开始计时
        self.time_starts = time.time()  # 这个是总计时，不能更改
        self.time_start = time.time()  # 这个是可以作为部分计时，可以更改

        # 因为要循环，因此肯定是前两个泵进行循环操作，而后洗涤的泵就开启时间较晚
        print("开启第一二个泵")

        print(f"self.time3：{self.time3-2}")

        # 开启阀门
        print('开启阀门')
        # 开启第三个泵
        print("开启第三个泵")

        # 计算物料输送结束的时间t3
        print(f"self.pump1_runtime：{self.pump1_runtime}")
        print("关闭第一二个泵")
        if next_unit:
            print("关闭第前泵")

        self.time = self.pump3_runtime-self.pump1_runtime
        print(f"self.time：{self.time}")

        # 开启第四个泵
        print("开启第四个泵")
        # 关闭阀门
        print('关闭阀门')
        # 开启第五个泵
        print("开启第五个泵")
        
        print(f"self.time6：{self.time6}")        
        
        # 关闭第三个泵
        print("关闭第三个泵")

        print(f"self.pump4_runtime：{self.pump4_runtime}")
        # 关闭第四个泵
        print("关闭第四个泵")

        # 抽取完流下的液体
        time.sleep(5)
        # 关闭第五个泵
        print("关闭第五个泵")
