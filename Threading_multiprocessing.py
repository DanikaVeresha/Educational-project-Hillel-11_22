
import datetime
from threading import Thread
from multiprocessing import Process


def countTicket(start, end):
    count = 0
    for item in range(start, end):
        num = str(item).rjust(6, '0')
        if int(num[0]) + int(num[1]) + int(num[2]) == int(num[3]) + int(num[4]) + int(num[5]):
            count += 1
    print(f'${count}$')
    return count


if __name__ == '__main__':
    time = datetime.datetime.now()
    countTicket(0, 1000000)
    print(f'${datetime.datetime.now() - time}$') # 0:00:01.673802

    print(f'-------------------------------')

    time = datetime.datetime.now()
    t1 = Thread(target=countTicket, args=[0, 250000])
    t2 = Thread(target=countTicket, args=[250000, 500000])
    t3 = Thread(target=countTicket, args=[500000, 750000])
    t4 = Thread(target=countTicket, args=[750000, 1000000])

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print(datetime.datetime.now() - time) # 0:00:01.306057

    print(f'-------------------------------')

    time = datetime.datetime.now()
    t1 = Process(target=countTicket, args=(0, 250000))
    t2 = Process(target=countTicket, args=(250000, 500000))
    t3 = Process(target=countTicket, args=(500000, 750000))
    t4 = Process(target=countTicket, args=(750000, 1000000))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print(datetime.datetime.now() - time) # 0:00:01.188846
