import multiprocessing
import os
import concurrent
from concurrent.futures import ProcessPoolExecutor
from runFunc import runTest

cmds = dict(java='javac Java.java;java Java',
            go='go run go.go',
            nodejs='node node.js',
            python='python python.py',
            perl='perl perl.pl')

pool = multiprocessing.Pool(processes=10)


def main():
    for (key, value) in cmds.items():
        pool.apply_async(runTest, (value, key))
    pool.close()
    pool.join()


def main2():
    with ProcessPoolExecutor(max_workers=15) as executor:
        future_to_result = {executor.submit(
            runTest, *(value, key)): key for (key, value) in cmds.items()}

        for future in concurrent.futures.as_completed(future_to_result):
            try:
                result = future.result()
                # print(result)
            except Exception as exc:
                print(exc)
            else:
                pass


if __name__ == '__main__':
    main2()
