#!/usr/bin/env python3
import os
import subprocess
import datetime
import filecmp

dir = "/home/poogas/j"

fname = os.listdir(dir)

for i in fname:
    fpath = os.path.abspath(f'{dir}/{i}')
    with open(fpath, 'r') as file:
        list = file.read().splitlines()
        for i in list:
            if '$Date:' in i:
                subprocess.run(['sed', '-i', '4d', fpath])

def getd(index):
    def foo(strf):
        return datetime.datetime.today().strftime(strf)

    def count(index):
        day = foo('%d')
        return int(day) - index

    return foo(f'%Y-%-m-{count(index)}')

yday, today = [], []

for i in fname:
    fpath = os.path.abspath(f'{dir}/{i}')
    if getd(1) in i:
        yday.append(fpath)
    if getd(0) in i:
        today.append(fpath)

yday, today = sorted(yday), sorted(today)

try:
    for i in range(len(today)):
        if filecmp.cmp(today[i], yday[i]):
            print(yday[i], 'Clear')
            os.remove(yday[i])
except IndexError:
    print('Done')
