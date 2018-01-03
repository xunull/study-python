from time import sleep, ctime
import _thread


def loop0():
    print('start loop 0 at: %s', ctime())
    sleep(4)
    print('loop 0 end at: %s', ctime())


def loop1():
    print('start loop 1 at: %s' % ctime())
    sleep(2)
    print('loop 1 end at: %s' % ctime())


def main():
    print("starting at: %s " % ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(6)
    print("all done at: %s" % ctime())


if __name__ == '__main__':
    main()
