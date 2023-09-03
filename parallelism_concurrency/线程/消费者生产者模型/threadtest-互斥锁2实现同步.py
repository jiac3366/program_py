from threading import Thread, Lock


def sale2(number):
    global tickets
    while True:
        with lock:
            if tickets > 0:
                print(f"窗口00{number}正在出售第{tickets}张票...")
                tickets -= 1
                if tickets == 0:
                    break
            else:
                print(f"窗口00{number}车票已销售完毕,谢谢.")
                break


if __name__ == '__main__':
    tickets = 100000
    lock = Lock()
    threads = []

    for index in range(1, 11):
        thread = Thread(target=sale2, args=(index,))
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()

    print(f"剩余票数: {tickets}")
