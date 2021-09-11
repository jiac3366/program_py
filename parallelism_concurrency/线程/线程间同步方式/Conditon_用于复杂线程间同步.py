# wait() 一定是被notify()唤醒的
# Condition线程的启动顺序十分重要
# eg:天猫精灵和小爱同学的对话

# 天猫：小爱同学
# 小爱：在

# 这时要先启动小爱线程
# Condition源码：
# wait()会释放Condition的底层锁 eg:天猫wait() 使得小爱能够执行'with condition:'语句
# 而又会创建一把上层锁 放入deque，每当notify()执行一次，就释放一把deque里面的锁 让其他调用了wait()操作的线程进一步执行
# 进一步了解Condition 请看Semaphores和Queue相关的源码