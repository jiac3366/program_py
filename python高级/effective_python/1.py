# 28
# 推导表达式：最多只有2个子表达式（2个if/2个for/1个if+1个for）
a = [i for i in range(1, 11)]
b = [x for x in a if x > 4 if x % 2 == 0]  # 默认if的关系是and

# 30
def index_of_word(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset  # 每次会按照\n分割文件中的每行line,此函数占用的最大内存就是文件中最长的句子
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset
    # import itertools
    #
    #     with open('1.txt', 'r') as f:
    #         it = index_file(f)
    #         result = itertools.islice(it, 0, 10)
    #         print(list(result))


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield line


def normalieze_iter(get_iter):
    it = get_iter()  # New iterator
    result = []
    for v in get_iter():  # New iterator
        length = len(v)
        result.append(length)
    return result


if __name__ == '__main__':
    # # 改进前：
    # it = read_visits('1.txt')
    # print(list(it))  # 相当于一次性走完了
    # print(list(it))
    # # ['hey your motherfucker\n', 'you better put you motherfucker shit on you motherfucker car']
    # # []
    #
    # # 方法一改进：
    # res = normalieze_iter(lambda: read_visits('1.txt'))
    # print(res)
    # print(res)

    # 方法二：定义一个容器类 每次需要一次列表就实现一次__iter__()  唯一缺点，就是多次读取输入数据
    class ReadVisits:
        def __init__(self, data_path):
            self.data_path = data_path

        def __iter__(self):
            with open(self.data_path) as f:
                for line in f:
                    yield int(line)

