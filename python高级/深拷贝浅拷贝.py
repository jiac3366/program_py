# 浅拷贝的方法--运用数据类型本身的构造器 或者 copy.copy()
# 不可变类型：有数字、字符串、元祖  复制永远（无论浅深拷贝）都是只复制指针  浅拷贝情况下嵌套内的元素性质却完全相反 不可变的变成可变 可变变成不可变
# 可变类型：列表、集合、字典  复制（无论浅深拷贝）出2个不同的对象
import copy

print("dict")
d1 = {1: 2, 2: 4, 3: 6}
d2 = dict(d1)
d3 = copy.deepcopy(d1)

# l2:[1, 2, 3]
print(d1 == d2)
# True
print(d1 is d2)
# False
print(d1 is d3)
# False
# ----------------------------------
print("list")
l1 = [1, 2, 3]
l2 = list(l1)
l3 = copy.deepcopy(l1)

# l2:[1, 2, 3]
print(l1 == l2)
# True
print(l1 is l2)
# False
print(l1 is l3)
# False
# ----------------------------------
print("set")
s1 = set([1, 2, 3])
s2 = set(s1)
s3 = copy.deepcopy(s1)
# s2:{1, 2, 3}
print(s1 == s2)
# True
print(s1 is s2)
# False

print(s1 is s3)
# False
# ----------------------------------
print("tuple")
t1 = (1, 2, 3)
t2 = tuple(t1)
t3 = copy.deepcopy(t1)
print(t1 == t2)
# True
print(t1 is t2)
# True
print(t1 is t3)
# True
# ----------------------------------
print("str")
s1 = "123"
s2 = str(s1)
s3 = copy.deepcopy(s1)
# 如果内容相等时 s1和s2指向相同的内存
# 当对s2进行修改时 就会申请2块不同的内存了
# s2 = s2+'22'
# print(s1) # False
# print(s2) # False
print(s1 == s2)
# True
print(s1 is s2)
# True
print(s1 is s3)
# True
s4 = s1 + "1"
s5 = s4[:len(s4)-1]
print(s1 is s5)
# False 不可变类型 修改的时候会重新开辟内存 变量的引用指向这块地址
# ----------------------------------
print("num")
n1 = 1
n2 = int(n1)
print(n1 == n2)
# True
print(n1 is n2)
# True
# ----------------------------------
# 嵌套中的浅拷贝（副作用）
print("copy")
L1 = [[1, 2], (3, 4)]
L2 = copy.copy(L1)
L3 = copy.deepcopy(L1)

print(L1 == L2)  # True
print(L1 is L2)  # False
print(L1 is L3)  # False
L1.append(100)
L1[0].append(3)
print(L1)
print(L2)

# L1： [[1, 2, 3], (3, 4), 100]
# L2： [[1, 2, 3], (3, 4)]
# 因为 l2 和 l1 作为整体是两个不同的对象，但内部的list是可变类型却会变
L1[1] += (5, 6)
print(L1)
print(L2)
# L1：[[1, 2, 3], (3, 4, 5, 6), 100]
# L2：[[1, 2, 3], (3, 4)]
# 内部的不可变元素真他吗不可变了
# ----------------------------------
# 嵌套中深拷贝 --对比嵌套中浅的拷贝 雷打不动
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


