
# 发布者
import time
import zmq


def run():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    # 同一个地址端口 bind 只能有一个，但却可以有很多个 connect 链接到这个地方
    socket.bind('tcp://*:6666')

    cnt = 1

    while True:
        time.sleep(1)
        socket.send_string('publish2: server cnt {}'.format(cnt))
        print('send {}'.format(cnt))
        cnt += 1


if __name__ == '__main__':
    run()

########## 输出 ##########
#
# send 1
# send 2
# send 3
# send 4
# send 5