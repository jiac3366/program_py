# -*- coding: utf-8 -*-

def reverse(x):
    num = 0
    while (x != 0):
        tmp = x % 10

        if num < -214748364 or (num == -214748364 and tmp < -8):
            return 0

        if num > 214748364 or (num == 214748364 and tmp > 7):
            return 0

        num = num * 10 + tmp
        x = int(x / 10)
    return num


# class Solution {
#     public int reverse(int x) {
#         int res = 0;
#         while(x!=0) {
#             //每次取末尾数字
#             int tmp = x%10;
#             //判断是否 大于 最大32位整数
#             if (res>214748364 || (res==214748364 && tmp>7)) {
#                 return 0;
#             }
#             //判断是否 小于 最小32位整数
#             if (res<-214748364 || (res==-214748364 && tmp<-8)) {
#                 return 0;
#             }
#             res = res*10 + tmp;
#             x /= 10;
#         }
#         return res;
#     }
# }


if __name__ == '__main__':
    # reverse(-123)
    print(-123 % 10)
