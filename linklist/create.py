class LNode:
    def __init__(self, num):
        self.data = num
        self.next = None


def create_link():
    """
    创建链表
    :return:
    """
    i = 1
    header = LNode(0)
    header.next = None
    cur = header

    while i < 8:
        lnode = LNode(i)
        lnode.next = None
        cur.next = lnode
        cur = lnode
        i += 1
    return header


def print_link(Node):
    cur = Node
    while cur:
        print(cur.data)
        cur = cur.next


if __name__ == '__main__':
    header = create_link()
    print_link(header)
