# from pudb import set_trace; set_trace()
from typing import List
import threading


class FooBar1:
    def __init__(self, n):
        """Using events. 104 ms, 27% ranking.
        """
        self.n = n
        self.events = [threading.Event(), threading.Event()]

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.events[0].clear()
            self.events[1].set()
            self.events[0].wait()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.events[1].wait()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.events[1].clear()
            self.events[0].set()


class FooBar2:
    def __init__(self, n):
        """Using Condition, 77 ms, 41% ranking.
        """
        self.n = n
        self.condition = threading.Condition()
        self.turn = 1
        self.foo_turn = lambda: self.turn == 1
        self.bar_turn = lambda: self.turn == -1

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.condition:
                self.condition.wait_for(self.foo_turn)
                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
                self.turn *= -1
                self.condition.notify()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.condition:
                self.condition.wait_for(self.bar_turn)
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()
                self.turn *= -1
                self.condition.notify()


class FooBar3:
    def __init__(self, n):
        """Using Lock
        """
        self.n = n
        self.foo_printed = threading.Lock()
        self.bar_printed = threading.Lock()
        self.foo_printed.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bar_printed.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.foo_printed.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_printed.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.bar_printed.release()


class FooBar4:
    def __init__(self, n):
        """Using Semaphore
        """
        self.n = n
        self.foo_printed = threading.Semaphore(0)
        self.bar_printed = threading.Semaphore(1)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bar_printed.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.foo_printed.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_printed.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.bar_printed.release()


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
