# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 09:50:52 2017

@author: ZHENGHAN ZHANG
"""
import os

# first construct the Particle class
class Particle:
    def __init__(self,pair1,pair2,e):
        self.coordinates = pair1
        self.vcoordinates = pair2
        self.identifier = e
    def move(self):
        self.coordinates += self.vcoordinates
#construct the board class        
class Board:
    def __init__(self, x, y):
        self.a=[]
        for i in range(x):
            self.b = []
            for j in range(y):
                self.b.append('')
            self.a.append(self.b)
        
    def update_board(self,particle):
        y = particle.coordinates.b
        x = particle.coordinates.a
        self.a[y][x]=particle.identifier 
        
    def __str__(self):
        m ='+-' * len(self.a[0]) + '+' +'\n'
        for i in self.a:
            for j in i:
                if j != '':
                    m +='|' + j
                else:
                    m += '|' + ' '
            m += '|'
            m += '\n'
            m +='+-' * len(self.a[0]) + '+' +'\n'
        return m


#pair class
class Pair:
    def __init__(self,x,y):
        self.a = x
        self.b = y
    def __add__(self,pair):
        pairNew = Pair(0,0)
        pairNew.a = self.a + pair.a
        pairNew.b = self.b + pair.b
        return pairNew
             
#Global code
pair1 = Pair(0,0)
pair2 = Pair(1,1)
p=Particle(pair1,pair2,'o')


for i in range(10):
    os.system('cls')
    b = Board(10,10)
    b.update_board(p)
    print(b)
    p.move()
