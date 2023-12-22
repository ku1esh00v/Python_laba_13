#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def harmonica(*args):
    """
    Функция находит среднее гармоническое аргументов
    """
    if args:
        values = [float(arg) for arg in args]
        count = 0
        for value in values:
            count += 1/value
        return round(len(values)/count, 4)
    else:
        return None


if __name__ == "__main__":
    print(harmonica(4, 8, 16))
    print(harmonica(3, 9, 27))
    print(harmonica(2, 3, 4))
    print(harmonica(31, 12, 32))
    print(harmonica(5))
    print(harmonica())
