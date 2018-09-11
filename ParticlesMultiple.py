# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 09:50:52 2017

@author: ZHENGHAN ZHANG
"""
import os

# first construct the Particle class
class Particle:
    def __init__(self,a,b,c,d,e):
        self.x = a
        self.y = b
        self.xVelocity = c
        self.yVelocity = d
        self.identifier = e
    def move(self):
        self.x += self.xVelocity
        self.y += self.yVelocity
        
class Board:
    def __init__(self, x, y):
        self.a=[]
        for i in range(x):
            self.b = []
            for j in range(y):
                self.b.append('')
            self.a.append(self.b)

        
    def update_board(self,particle):

        self.a[particle.y][particle.x]=particle.identifier 
        
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
            
#Global code
p=Particle(0,0,1,1,'o')
p2 = Particle(9,9,-1,-1,'*')

for i in range(10):
    os.system('cls')
    b = Board(10,10)
    b.update_board(p)
    b.update_board(p2)
    print(b)
    p.move()
    p2.move()
