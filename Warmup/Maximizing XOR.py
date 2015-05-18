#!/bin/python

# Complete the function below.


def  maxXor(_l, _r):
    max=0
    for A in range(_l,_r+1):
        for B in range(A,_r+1):
            if A^B>max:
                max=A^B
    return max

    

_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)