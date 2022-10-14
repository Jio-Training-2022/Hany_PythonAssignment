#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    #Sun 10 May 2015 13:54:36 -0700
    fmt = "%a %d %b %Y %H:%M:%S %z"
    #making the input string of type datetime
    ti1 = datetime.strptime(t1,fmt)
    ti2 = datetime.strptime(t2,fmt)
    return str(int(abs((ti1 - ti2).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
