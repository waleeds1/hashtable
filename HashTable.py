#!/usr/bin/env python
# coding: utf-8

class HashTable:
    def __init__(self,m):
        self.table=[None]*m
        self.n=0
        self.m=m
    
    def __ReHash(self):
        if self.__LF() > 0.75:
            newTable=[None]*(2*self.m)
        elif self.__LF() <= 0.1:
            newTable=[None]*(self.m//2)
        for i in range(self.m):
            if self.table[i] is not None:
                key=self.table[i][0]
                if type(key) == int or (type(key) == str and key.isdigit()):
                    ind=int(key)%len(newTable)
                    j=7-(int(key)%7)
                    while newTable[ind] is not None:
                        ind=(ind+j)%len(newTable)
                else:
                    val=0
                    n=len(key)
                    for j in str(key):
                        if j.isdigit() is True:
                            val+=int(j)
                        else:
                            n-=1
                            val+=ord(j)*10**(n)
                    ind=val%len(newTable)
                    j=7-(val%7)
                    while newTable[ind] is not None:
                        ind=(ind+j)%len(newTable)
                newTable[ind]=self.table[i]
                    
        self.table=newTable
        self.m=len(newTable)
    
    def __HashFunction(self,key,function):
        val=0
        index=0
        
        if type(key) == int or (type(key) == str and key.isdigit()):
            index= int(key)%self.m
            j=7-(int(key)%7)
            if function == "ins":
                while self.table[index] is not None:
                    index=(index+j)%self.m
            elif function == "search":
                if self.table[index] is not None and self.table[index][0] == key:
                    return index
                else:
                    x=0
                    found=False
                    while x!=self.n and found is False:
                        index=(index+j)%self.m
                        if self.table[index] is not None and self.table[index][0] == key:
                            found=True
                        x+=1
                    if found == False:
                        return False
                    else:
                        return index
                        
                
        else:
            n=len(key)
            for i in str(key):
                if i.isdigit() is True:
                    
                    val+=int(i)
                else:
                    n-=1
                    val+=ord(i)*10**(n)
            index=val%len(self.table)
            j=7-(val%7)
            if function == "ins":
                while self.table[index] is not None:
                    index=(index+j)%self.m
            elif function == "search":
                if self.table[index] is not None and self.table[index][0] == key:
                    return index
                else:
                    x=0
                    found=False
                    while x!=self.n and found is False:
                        index=(index+j)%self.m
                        if self.table[index] is not None and self.table[index][0] == key:
                            found=True
                        x+=1
                    if found == False:
                        return False
                    else:
                        return index
        
        return index
    def Insert(self,key,value):
        if self.__LF()>0.75:
                self.__ReHash()
        self.n+=1
        self.table[self.__HashFunction(key,'ins')]=(key,value)
    
    def Search(self,key):
        ind=self.__HashFunction(key,"search")
        if ind is False:
            print("Key not found!")
        else:
            return self.table[ind][1]
    
    def Delete(self,key):
        y=None
        ind=self.__HashFunction(key,"search")
        if ind is False:
            print("Key not found!")
        else:
            y=self.table[ind]
            self.table[ind]=None
            self.n-=1
        if self.__LF()<=0.1 and len(self.table)//2 >7:
                self.__ReHash()
        return y
    def __LF(self):
        LF= self.n/self.m
        return LF
            
        
    def PrintTable(self):
        print('{:20}{:20}'.format('key','data'))
        for i in self.table:
            if i is not None:
                print('{:20}{}'.format(i[0],i[1]))
    def PrintArray(self):
        print(self.table)
