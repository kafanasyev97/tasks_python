from collections import Counter


def can_be_poly(val: str) -> bool:
    return len(list(filter(lambda x: x % 2, Counter(val).values()))) <= 2


if __name__ == '__main__':
    print(can_be_poly('abcba'))
    print(can_be_poly('abbbc'))
