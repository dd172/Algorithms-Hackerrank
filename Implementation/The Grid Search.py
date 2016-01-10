 #!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in xrange(R):
       G_t = str(raw_input().strip())
       G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in xrange(r):
       P_t = str(raw_input().strip())
       P.append(P_t)
    flag = 0
    n=0
    #print R,C,r,c,R-r,C-c
    for i in range(R-r+1):
        if flag:
            break
        for j in range(C-c+1):
            if flag:
                break
            if G[i][j:j+c] == P[n]:
                #print G[i][j:j+c],P[n],i,j,'an candidate is found,continue searching next line'

                for y in range(1,r+1):
                    n+=1
                    if n == r:
                        #print 'the candidate matches all of the line and accepted'
                        flag=1
                        break
                    #print G[i+1][j:j+c],i+1,j,'now check the next line '
                    #print 'runs to',i+y,n,G[i+y][j:j+c],P[n]
                    if G[i+y][j:j+c]== P[n]:
                        pass
                        #print n,r,'the line matches and go next'
                        
                    else:
                        n=0
                        #print 'the candidate does not match the next line'
                        break
    if flag:
      print 'YES'
    else:
      print 'NO'
  
