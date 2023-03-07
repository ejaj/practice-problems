#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : coroutine.py
@Time : 3/31/22 11:48 PM
@Desc: 
"""

'''
def func():
    print("Function Starts")
    yield
    print("Function End")
'''


def func():
    x = 5
    print('Function Part 1')
    yield x

    x += 7
    print('Function part 2')
    yield x
    print('Function part 3')


def bare_bones():
    print("My first Coroutine!")
    while True:
        value = (yield)
        print(value)


# Passing Argument
def filter_line(num):
    while True:
        line = (yield)
        if num in line:
            print(line)


# The StopIteration Exception
def test():
    while True:
        value = (yield)
        print(value)


# Coroutines with Decorators
def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr

    return start


@coroutine
def bare():
    while True:
        value = (yield)
        print(value)


def main():
    '''
    try:
        y = func()
        z = next(y)
        print(z)

        z = next(y)
        print(z)

        z = next(y)
        print(z)

    except StopIteration as e:
        pass
    '''
    # coroutine = bare_bones()
    # next(coroutine)
    # coroutine.send("First Value")
    # coroutine.send("Second Value")
    # coroutine.close()

    # cor = filter_line("33")
    # next(cor)
    # cor.send("Jessica, age:24")
    # cor.send("Marco, age:33")
    # cor.send("Filipe, age:55")
    # try:
    #     cor = test()
    #     next(cor)
    #     cor.close()
    #     cor.send("So Good")
    # except StopIteration:
    #     print("Done with the basics")

    cor = bare()
    cor.send("Using a decorator!")
if __name__ == '__main__':
    main()
