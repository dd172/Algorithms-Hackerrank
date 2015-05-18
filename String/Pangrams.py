#!usr/env/bin python

def solution(S):
    flag=1
    s=S.lower()
    for i in range(97,123):
        if s.find(chr(i))==-1:
            flag=0
    if flag:
        print "pangram"
    else:
        print "not pangram"
if __name__ == '__main__':
    S=raw_input()
    solution(S)
  