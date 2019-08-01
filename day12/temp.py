import threading
import time


def worker(arg):
    while True:
        print("I'm working {}".format(arg))
        time.sleep(1)

    print("Fineshed")


t = threading.Thread(target=worker, args=(threading.current_thread(),), name="firstworker")
t1 = threading.Thread(target=worker, args=("1",), name="")
t2 = threading.Thread(target=worker, args=("2",), name="")
t3 = threading.Thread(target=worker, args=("3",), name="")
# t = threading.Thread(target=worker, args=(threading.current_thread(),), name="")
t.start()
t1.start()
t2.start()
t3.start()