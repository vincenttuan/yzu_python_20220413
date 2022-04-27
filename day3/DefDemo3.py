# 自訂函數篇
# r: 半徑
# return area(圓面積), volume(球體積)
import math
import day3.NumberUtil as nu
def calcAreaAndVolume(r):
    area = r**2 * math.pi
    volume = 4/3 * math.pi * r**3
    return area, volume


if __name__ == '__main__':
    r = 15
    area, volume = calcAreaAndVolume(r)
    # 小數點一位
    print('圓面積: %.1f' % area)
    print('球體積: %.1f' % volume)
    # 加上千分號
    print('圓面積: %s' % format(area, ','))
    print('球體積: %s' % format(volume, ','))
    # 加上千分號 + 小數點一位
    print('圓面積: %s' % format(float('%.1f' % area), ','))
    print('球體積: %s' % format(float('%.1f' % volume), ','))

    print(nu.get(area, 2))
    print(nu.get(volume, 2))

