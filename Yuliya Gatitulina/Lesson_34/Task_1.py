import threading #Different values as a result, because t2 may or may not start running before t1 is completed

class Counter(threading.Thread):
    counter = 0
    rounds = 100000


    def run(self):
        for i in range(Counter.rounds):
            Counter.counter += 1
        print(Counter.counter)

t1 = Counter()
t2 = Counter()
t1.start()
t2.start()
t1.join()
t2.join()
