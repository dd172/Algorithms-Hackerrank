# -*-coding:utf-8 -*-  
#加权并查集算法  
class WeightedUF():  
    fatherid=[]  
    sz=[]  
    count=0  
    def __init__(self,n):  
        self.count=n  
        self.fatherid=[i for i in range(n)]  
        self.sz=[0 for i in range(n)]  
    def getcount(self):  
        return self.count  
    def connected(self,p,q):  
        return self.find(p)==self.find(q)  
    def find(self,p):  
        while p !=self.fatherid[p]:  
            p=self.fatherid[p]  
        return p  
    def pathcompressionfind(self,p):  
        if p==self.fatherid[p]:  
            return p  
        else:  
            self.fatherid[p]=self.pathcompressionfind(self.fatherid[p])  
            return self.fatherid[p]  
    def union(self,p,q):  
        i=self.find(p)  
        j=self.find(q)  
        if i==j:  
            return   
        if self.sz[i]<self.sz[j]:  
            self.fatherid[i]=j  
            self.sz[j]+=self.sz[i]  
        else:  
            self.fatherid[j]=i  
            self.sz[i]+=self.sz[j]  
        self.count-=1  
  
  
x=WeightedUF(10)  
x.union(9,2)  
x.union(9,3)  
x.union(1,2)  
x.union(5,2)  
print x.getcount()  
  
print x.connected(9,4)  
print x.connected(9,5)