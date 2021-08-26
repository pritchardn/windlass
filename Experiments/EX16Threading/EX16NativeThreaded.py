import datetime
from multiprocessing import Pool

from dlg.apps.simple import ListAppendThrashingApp
from dlg.drop import InMemoryDROP


def test_iteration(pid: int):
    drop = ListAppendThrashingApp(oid=1, uid=23, size=8000)
    memory_drop = InMemoryDROP(oid=2, uid=2)
    drop.addOutput(memory_drop)
    drop.run()


def test(count=4):
    with Pool(processes=count) as pool:
        pool.map(test_iteration, range(count))


def main():
    for i in range(10):
        tic = datetime.datetime.now()
        test()
        toc = datetime.datetime.now()
        print(f"{tic.time()} {toc.time()}")


if __name__ == '__main__':
    main()
