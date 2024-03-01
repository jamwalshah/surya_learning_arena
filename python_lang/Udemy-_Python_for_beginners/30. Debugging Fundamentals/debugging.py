# debugging.py

from mymodule import fun2
def fun1(n):
    print('fun1', n)                        # breakpoint here
    fun2(n)

n = int(input('Enter a number:')) # 0       # breakpoint here
fun1(n)