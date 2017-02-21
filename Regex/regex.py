#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jihyunkim
netID: jk4704
NLP Assignment 2

"""

import re

regex_in, input_file = input().split()

source = input_file
which = regex_in[6:]
out = 'output_' + which + '.txt'
out_list = which + '.txt'

count = 0
with open (regex_in, 'r') as regex_file:
    regex_open = regex_file.read()
regex = re.compile(regex_open)

try:
    f = open(source, 'r')
except:
    print("The text corpos cannot be opened or read.")
else:
    t1 = open(out,'w')
    t2 = open(out_list,'w')

    for line in f:
        result = regex.search(line)
        if result:
            result_str = result.group(0).strip()
            count += 1
            line = re.sub(regex, r'[\1]\n', line)
            t1.write(line)
            t2.write(result_str +'\n')
            print('Found '+str(count))

    t2.write('Total found: ' + str(count))
    f.close()
    t1.close()
    t2.close()
