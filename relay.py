#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
"""
引脚与阀门对应的关系图
{
引脚：阀门
11：第一个


}
"""


class Value():
    def __init__(self, pin) -> None:
        # 定义继电器引脚为pin
        self.markerobo_RelayPin = pin
        self.makerobo_setup()

    # 初始化工作
    def makerobo_setup(self):
        GPIO.setmode(GPIO.BOARD)  # 采用实际的物理引脚给GPIO口
        GPIO.setup(self.markerobo_RelayPin, GPIO.OUT)  # 设置pin模式为输出模式
        GPIO.output(self.markerobo_RelayPin, GPIO.LOW)  # 关闭继电器

    # 循环函数
    def value_start(self):
        # 继电器断开
        GPIO.output(self.markerobo_RelayPin, GPIO.HIGH)
        
    def value_stop(self):
        GPIO.output(self.markerobo_RelayPin, GPIO.LOW)
    
    # test
    def test_realy(self):
        while True:
            GPIO.output(self.markerobo_RelayPin, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(self.markerobo_RelayPin, GPIO.LOW)
            time.sleep(0.5)

    # 释放资源
    def value_end(self):
        GPIO.output(self.markerobo_RelayPin, GPIO.LOW)
        GPIO.cleanup()


# # 主程序
# if __name__ == "__main__":
#     test = Value(12)
#     try:
#         # test.value_start()
#         test.test_realy()
#     except:
#         test.value_end()
