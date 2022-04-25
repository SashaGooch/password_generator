# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 01:33:59 2022

@author: gocan
"""

# # Password generator

import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
symbol = '[]{}()-_.#;*'

all = lower + upper + number + symbol
length = 9

password = "".join(random.sample(all,length))
print(f'Random generated password provided by SashaGooch: {password}')