#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
Anniversary
"""

from datetime import date


def main():
    """pass"""
    hrt = date(2017, 2, 8)
    liu = date(2017, 3, 31)
    res = date(2022, 7, 5)
    hrtdelta = date.today() - hrt
    liudelta = date.today() - liu
    resdelta = res - date.today()
    print('HRT: {delta:6d}'.format(delta=hrtdelta.days))
    print('LIU: {delta:6d}'.format(delta=liudelta.days))
    print('RES: {delta:6d}'.format(delta=resdelta.days))


if __name__ == '__main__':
    main()
