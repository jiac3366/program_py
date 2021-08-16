# 浅拷贝的方法--运用数据类型本身的构造器 或者 copy.copy()
import copy
print("list")
l1 = [1, 2, 3]
l2 = list(l1)

# l2:[1, 2, 3]
print(l1 == l2)
# True
print(l1 is l2)
# False
# ----------------------------------
print("set")
s1 = set([1, 2, 3])
s2 = set(s1)
# s2:{1, 2, 3}

print(s1 == s2)
# True
print(s1 is s2)
# False
# ----------------------------------
print("tuple")
t1 = (1, 2, 3)
t2 = tuple(t1)
print(t1 == t2)
# True
print(t1 is t2)
# True
# ----------------------------------
print("str")
s1 = "123"
s2 = str(s1)
# 当对s2进行修改时 就会申请2块不同的内存了
# s2 = s2+'22'
# print(s1) # False
# print(s2) # False
print(s1 == s2)
# True
print(s1 is s2)
# ----------------------------------
print("num")
n1 = 1
n2 = int(n1)
print(n1 == n2)
# True
print(n1 is n2)
# ----------------------------------
# 嵌套中的浅拷贝（副作用）
print("copy")
L1 = [[1, 2], (3, 4)]
L2 = copy.copy(L1)
L1.append(100)
L1[0].append(3)
print(L1)
print(L2)
# [[1, 2, 3], (3, 4), 100]
# 因为 l2 和 l1 作为整体是两个不同的对象
# [[1, 2, 3], (3, 4)]
L1[1] += (5, 6)
print(L1)
print(L2)
# [[1, 2, 3], (3, 4, 5, 6), 100]
# [[1, 2, 3], (3, 4)]
# ----------------------------------
# 嵌套中深拷贝
print("deepcopy")
L1 = [[1, 2], (3, 4)]
L2 = copy.deepcopy(L1)
L1.append(100)
L1[0].append(3)
print(L1)
print(L2)
# [[1, 2, 3], (3, 4), 100]
# [[1, 2], (3, 4)]
L1[1] += (5, 6)
print(L1)
print(L2)
# [[1, 2, 3], (3, 4, 5, 6), 100]
# [[1, 2], (3, 4)]
