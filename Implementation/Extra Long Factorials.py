#!/bin/python
#recursion

import sys


n = int(raw_input().strip())


def cal(n):

	if n==1:
		return 1
	else:
		return n*cal(n-1)

print cal(n)
