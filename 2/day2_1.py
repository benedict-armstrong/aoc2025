#!/usr/bin/env python3

numer_of_safe_reports = 0


def is_safe_report(line: str) -> int:
    numbers = list(map(int, line.split()))
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
        numer_of_safe_reports += is_safe_report(line)

print(numer_of_safe_reports)
