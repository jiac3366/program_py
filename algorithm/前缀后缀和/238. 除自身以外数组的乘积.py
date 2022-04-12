# coding=utf-8

def func():
    s = [1, 2, 3, 4]
    qianzhuihe = [0] * len(s)
    num = 1
    qianzhuihe[0] = 1
    for i in range(1, len(s)):
        num *= s[i-1]
        qianzhuihe[i] = num

    print(qianzhuihe)



if __name__ == '__main__':
    for i in range(9, -1, -1):
        print(i)
