#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_sum_between_negatives(*args):
    negative1_index = -1
    negative2_index = -1
    total_sum = 0

    for i, arg in enumerate(args):
        if arg < 0:
            if negative1_index == -1:
                negative1_index = i
            else:
                negative2_index = i
                break

    if negative1_index == -1 or negative2_index == -1:
        return None

    for arg in args[negative1_index + 1:negative2_index]:
        total_sum += arg

    return total_sum


if __name__ == '__main__':
    print(get_sum_between_negatives(1, 2, -3, 4, -5, 6))  # Output: 4
    print(get_sum_between_negatives(-1, -2, -3))  # Output: None
    print(get_sum_between_negatives())  # Output: None
