#!/usr/bin/py
def lonelyinteger(a):
    for _ in a:
        if a.count(_)==1:
            return _
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)