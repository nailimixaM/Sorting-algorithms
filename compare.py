import threading
import random
import quicksort
import bubblesort

class myThread(threading.Thread):
    def __init__(self,threadID,sorting_alg,x):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.sorting_alg = sorting_alg
        self.x = x
        print("Thread " + str(threadID) + " started.")
    
    def run(self):
        self.sorting_alg(self.x)
        print(self.x)

def main():
    print("Hello world")
    x = [random.random() for j in range(100)]
    
    thread1 = myThread(1,quicksort.quickSort,x)
    thread2 = myThread(2,bubblesort.bubbleSort,x)
    
    thread1.start()
    thread2.start()


if __name__ == "__main__":
    main()
