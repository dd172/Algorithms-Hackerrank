str1 = raw_input()

str2 = raw_input()

str0 = set(str1+str2)

sum = 0

for i in str0:
	
	j = str1.count(i)

	k = str2.count(i)

	x = abs(j-k)

	sum+=x

print sum