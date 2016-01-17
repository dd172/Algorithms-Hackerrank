#! bin/python
# function do_fake_rotation does not really rotates,only can get the right anwser of the request.
R,C,M = raw_input().strip().split(' ')
R,C,M = [int(R),int(C),int(M)]
G = []
G_i = 0
for G_i in xrange(R):
	G_t = raw_input().strip().split(' ')
	G.append(G_t)

def do_rotate(R,C,G):
	i,j=0,0
	while i < R/2 and j < C/2:
		
		temp = G[i][j]
		for n in range(C-2*j-1):
			G[i][j+n]=G[i][j+n+1]
		for n in range(R-2*i-1):
			G[i+n][C-j-1]=G[i+n+1][C-j-1]
		for n in range(C-2*i-1):
			G[R-i-1][C-j-1-n]=G[R-i-1][C-j-2-n]
		for n in range(R-2*i-1):
			G[R-i-1-n][j]=G[R-i-2-n][j]
		G[i+1][j]=temp
		i+=1
		j+=1

def do_fake_rotation(R,C,G,M):
	i,j = 0,0
	while i < R/2 and j < C/2:
		m = M%(2*C+2*R-4*i-4*j-4)
		l = []
		for n in range(C-2*j-1):
			l.append(G[i][j+n])
		for n in range(R-2*i-1):
			l.append(G[i+n][C-j-1])
		for n in range(C-2*i-1):
			l.append(G[R-i-1][C-j-1-n])
		for n in range(R-2*i-1):
			l.append(G[R-i-1-n][j])

		l=l[m:]+l[:m]
		k = 0
		for n in range(C-2*j-1):
			G[i][j+n]=l[k]
			k += 1
		for n in range(R-2*i-1):
			G[i+n][C-j-1]=l[k]
			k += 1
		for n in range(C-2*i-1):
			G[R-i-1][C-j-1-n]=l[k]
			k += 1
		for n in range(R-2*i-1):
			G[R-i-1-n][j]=l[k]
			k += 1
		i += 1
		j += 1


do_fake_rotation(R,C,G,M)

for i in G:
	for j in i:
		print j,
	print 