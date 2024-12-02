#!/usr/bin/env python3

import typing


numer_of_safe_reports = 0


def is_safe_report(numbers: typing.List[int]) -> int:
    asc = True
    if numbers[0] > numbers[1]:
        asc = False
    for i in range(1, len(numbers)):
        diff = numbers[i - 1] - numbers[i]
        if asc and (diff > -1 or diff < -3):
            return 0
        if not asc and (diff < 1 or diff > 3):
            return 0

    return 1


with open("input.txt") as f:
    for line in f:
        numbers = list(map(int, line.split()))
        if is_safe_report(numbers) == 0:
            for i in range(len(numbers)):
                without_i = numbers[:i] + numbers[i + 1 :]
                if is_safe_report(without_i):
                    numer_of_safe_reports += 1
                    break
        else:
            numer_of_safe_reports += 1

print(numer_of_safe_reports)
