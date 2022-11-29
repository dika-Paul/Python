from os import getpid, getppid
from multiprocessing import Process


def process_try(filename):
    print("pid of process is {}\n".format(getpid()))
    print("ppid of this process is {}\n".format(getppid()))
    print("process {} start working on {}\n".format(getpid(), filename))


def main():
    p1 = Process(target=process_try, args=("Windows", ))
    p1.start()
    p2 = Process(target=process_try, args=("Linux", ))
    p2.start()
    p1.join()
    p2.join()
    print("process finish")


if __name__ == "__main__":
    main()
