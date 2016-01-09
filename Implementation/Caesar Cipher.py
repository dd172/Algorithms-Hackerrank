#!/bin/python

import sys


n = int(raw_input())
s = raw_input().strip()
s = list(s)
print range(65,91)+range(97,123)
for i in range(65,91)+range(97,123):
	print chr(i),
print 

k = int(raw_input().strip())
k=k%26
for i in range(n):
	if ord(s[i]) in range(65,91)+range(97,123):

		if ord(s[i]) in range(65,91-k)+range(97,123-k):
			s[i] = chr(ord(s[i])+k)
		else:
			s[i] = chr(ord(s[i])+k-26)


print "".join(s)
