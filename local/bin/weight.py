#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

DATE_FROM = datetime.date(2019, 5, 5)
DATE_TILL = DATE_FROM + datetime.timedelta(7)
WEIGHT_FROM = 80.9
WEIGHT_TILL = WEIGHT_FROM - 0.3 * 7
DESIRED_VAL = WEIGHT_FROM + \
    (WEIGHT_TILL - WEIGHT_FROM) / \
    (DATE_TILL - DATE_FROM).days * \
    (datetime.date.today() - DATE_FROM).days

print('WEIGHT: %0.1f' % DESIRED_VAL)
