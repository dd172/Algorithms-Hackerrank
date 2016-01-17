#! bin/python
# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function
import sys

s = raw_input().strip()
type(s)
l = len(s)

row = 1

col = 1

while row*col < l:
	if col > row:
		row += 1
	else:
		col += 1

encryption=[([0]*col)for i in range(row)]

n = 0

for i in range(row):
	for j in range(col):
		if n<=l-1:
			encryption[i][j] = s[n]
			n+=1
		

for i in range(col):
	for j in range(row):
		if encryption[j][i]==0:
			pass
		else:
			print(encryption[j][i],end='')
	print(' ',end='')
