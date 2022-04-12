#!/usr/bin/env python3

import numpy as np


class MyProcessor:
    def __init__(self, exp):
        self.exp = exp

    def process(self, d: np.array):
        return d ** self.exp


def main():
    data = np.arange(0, 10)
    p = MyProcessor(exp=2)
    data_processed = p.process(data)
    print('data_processed: {}'.format(data_processed))


if __name__ == '__main__':
    main()
