import re 

t= int(raw_input())

line= raw_input()

sum=0

for n in re.findall(r'\d+',line):
	sum+=long(n)

print sum