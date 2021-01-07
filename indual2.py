# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Реализовать класс-оболочку Number для числового типа float. Реализовать методы
# умножения и вычитания. Создать производный класс Real, в котором реализовать метод,
# вычисляющий корень произвольной степени, и метод для вычисления числа pi в данной
# степени.

import math


class Number:
    def __init__(self, num=0):
        self.num = float(num)

    def sub(self, h):
        return Number(self.num - h.num)

    def mul(self, h):
        return Number(self.num * h.num)


class Real(Number):
    def __init__(self, num=0):
        super(Real, self).__init__(num)

    def sqrtn(self, n):
        return self.num ** (1 / n)

    def pow(self, h):
        return math.pi ** h.num

if __name__ == '__main__':
    r1 = Number(4)
    r2 = Real(16)
    r = r1.mul(r2)
    print("Метод умножения", r.num)
    r = r1.sub(r2)
    print("Метод вычитания",r.num)
    r = r2.sqrtn(2)
    print("Вычисление корня произвольной степени", r)
    r = r2.pow(r1)
    print("Вычисления числа pi в произвольной степени", r)