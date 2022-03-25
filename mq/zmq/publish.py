
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
        # 如果 把time.sleep(1)移动到while最后
        # 因为建立连接需要时间，建立成功之前的所有消息都会丢失: 第一条消息会丢失

        # 有多个发布者，ZMQ 应该怎么做?
        # 在 linux socket 中, 一个连接就是一个 socket , 但在 ZMQ 中, 一个 socket 上可以承载多个数据连接
        # 要把socket理解为程序员访问数据连接的一个入口。因此，我们在绑定一个 socket 之后，可以让多个发布者连接到这里即可，和多个订阅者的使用是同样的方式

        # 个人理解celery只是一种异步处理的工具，celery本身也是依赖其他消息队列的，
        # 比如服务器发送消息到中间件，如redis、RabbitMQ、Kafka等，celery worker向中间件订阅消息并从中取出进行处理
        time.sleep(1)
        socket.send_string('publish1: server cnt {}'.format(cnt))
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