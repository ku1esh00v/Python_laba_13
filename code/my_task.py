#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_values(**kwargs):
    """
    Функция выводит на экран аргументы (с их названиями), которые переданы в функцию
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")


if __name__ == '__main__':
    print_values(name="Oleg", age=19, city="Stavropool")
