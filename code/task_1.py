#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def geometric_sr(*args):
    """
    Функция ищет среднее геометрическое аргументов
    """
    if args:
        values = [float(arg) for arg in args]
        count = 1
        for value in values:
            count *= value
        return round(pow(count, 1/len(values)), 4)
    else:
        return None


if __name__ == "__main__":
    print(geometric_sr(4, 8, 16))
    print(geometric_sr(3, 9, 27))
    print(geometric_sr(2, 3, 4))
    print(geometric_sr(31, 12, 32))
