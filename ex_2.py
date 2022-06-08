#!/usr/bin/env python 3
# -*- config: utf-8 -*-

import sys

if __name__ == '__main__':
    dict = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", }
    dict_items = {j: i for i, j in dict.items()}
    print(dict, dict_items)