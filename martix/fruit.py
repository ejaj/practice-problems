#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : fruit.py
@Time : 7/22/22 1:29 AM
@Desc: 
"""


class Fruit:
    name = "Apple"
    price = 10

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def eat_fruit(self):
        print("Fruit is eaten")


f = Fruit("Orance", 10)
f.eat_fruit()
print(f.name)
print(f.price)
