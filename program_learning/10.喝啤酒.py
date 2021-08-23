# -*- coding: utf-8 -*-
# 现在有x瓶啤9  3空瓶子换瓶 7瓶盖换1瓶

def drinkhowmany(x):
    count = 0
    gaizi = 0
    pingzi = 0
    while x > 0:
        while gaizi >= 3:
            x += 1
            gaizi -= 3
        while pingzi >= 7:
            x += 1
            pingzi -= 7
        count += 1
        gaizi += 1
        pingzi += 1
        x -= 1

    print(count)
    return count


def drinkhowmany2(x): # 正确的
    count = x
    pingzi = x
    gaizi = x
    while pingzi >= 3 or gaizi >= 7:
        while pingzi >= 3:
            change = int(pingzi / 3)
            count += change
            pingzi %= 3
            gaizi += change
        while gaizi >= 7:
            change = int(gaizi / 7)
            count += change
            gaizi %= 7
            pingzi += change
    print(count)
    return count





if __name__ == '__main__':
    drinkhowmany(18)






