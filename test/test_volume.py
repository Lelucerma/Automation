def volume_time(volume, speed):
        volume = volume
        speed = speed
        pump_runtime = (volume / speed)*60 + 10
        return pump_runtime
a = volume_time(60,60)
print(a)