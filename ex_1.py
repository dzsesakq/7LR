#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    class_in_school = {'1a': 25, "2a": 30,'4a': 24, '5a': 23, '6a': 21, '7a': 18, '8a': 23, '8a': 15,  }

    class_in_school['1a'] = 22
    class_in_school['3a'] = 21
    del class_in_school['4a']
    print(class_in_school)

    f = sum(class_in_school.values())
    print(f)