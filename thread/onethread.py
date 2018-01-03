
from time import sleep, ctime

def loop1():
    print('loop1 start at: %s' % ctime())
    sleep(3)
    print('loop1 end at: %s' % ctime())

def loop2():
    print('loop2 start at: %s ' % ctime())
    sleep(2)
    print('loop2 end at: %s' % ctime())


def main():
    loop1()
    loop2()

if __name__ == '__main__':
    main()