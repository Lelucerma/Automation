import math


def tube_time(length, run_speed, diameter=0.5):
    """"
    根据泵的速度和需要进液的容量确定泵的运行时间，需要设置一定的时间冗余，
    对于泵停止所需要的时间需要进行相应的调整。需做出一个统计
    Args:
        * direction 泵的运行方向
        * speed 泵的运行速度

    """

    length = length  # 管道的长度
    diameter = diameter   # 管道的直径
    speed = run_speed
    tube_volume = length * math.pow((diameter/2), 2) * math.pi
    tube_time1 = tube_volume / speed / 0.8027 * 60
    return tube_time1


a = tube_time(23, 60)
print(a)
