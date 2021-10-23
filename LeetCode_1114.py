# from pudb import set_trace; set_trace()
from typing import List
from time import sleep
from threading import Barrier, Lock, Event, Semaphore, Condition


class Foo1:
    def __init__(self):
        self.semaphore = 0


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.semaphore += 1


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.semaphore != 1:
            sleep(0.1)
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.semaphore += 1


    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.semaphore != 2:
            sleep(0.1)
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


class Foo2:
    def __init__(self):
        self.barriers = (Barrier(2), Barrier(2))

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.barriers[0].wait()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.barriers[0].wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.barriers[1].wait()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.barriers[1].wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


class Foo3:
    def __init__(self):
        self.locks = (Lock(), Lock())
        self.locks[0].acquire()
        self.locks[1].acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.locks[0].release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.locks[0]:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.locks[1].release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.locks[1]:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()


class Foo4:
    def __init__(self):
        self.events = (Event(), Event())

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.events[0].set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.events[0].wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.events[1].set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.events[1].wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


class Foo5:
    def __init__(self):
        self.semaphores = (Semaphore(0), Semaphore(0))

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.semaphores[0].release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.semaphores[0]:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.semaphores[1].release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.semaphores[1]:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()


class Foo6:
    def __init__(self):
        self.cond = Condition()
        self.order = 0
        self.to_print_second = lambda: self.order == 1
        self.to_print_third = lambda: self.order == 2

    def first(self, printFirst: 'Callable[[], None]') -> None:
        with self.cond:
            # printFirst() outputs "first". Do not change or remove this line.
            printFirst()
            self.order += 1
            self.cond.notify_all()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.cond:
            self.cond.wait_for(self.to_print_second)
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.order += 1
            self.cond.notify_all()


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.cond:
            self.cond.wait_for(self.to_print_third)
            # printThird() outputs "third". Do not change or remove this line.
            printThird()



# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
