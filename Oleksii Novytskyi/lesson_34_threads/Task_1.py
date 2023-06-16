import threading

class Counter(threading.Thread):

    counter = 0
    rounds = 100000

    def run(self):

        for i in range(Counter.rounds):
            Counter.counter += 1
        return Counter.counter

t_1 = Counter()
t_2 = Counter()

print(t_1.counter)
print(t_2.counter)

t_1.start()
t_2.start()
t_1.join()
t_2.join()

print(t_1.counter)
print(t_2.counter)