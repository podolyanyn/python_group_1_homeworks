import threading


class Counter(threading.Thread):
    counter = 0  # shared variable to count the iterations
    rounds = 100000  # number of iterations to be performed in each thread

    def run(self):
        for i in range(Counter.rounds):  # a loop that goes through the rounds range to iterate
            Counter.counter += 1
        return Counter.counter


thread1 = Counter()
thread2 = Counter()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(thread1.counter)
print(thread2.counter)


