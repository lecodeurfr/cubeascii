#Cubeascii v2.0

#Fix list
#-inverted vertical constant line

import math as m
import keyboard as k
import os
import time

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getCoords(self):
        return self.x, self.y

    def move(self, xm, ym):
        self.x += xm
        self.y += ym

class Line():
    def __init__(self, point1, point2):
        self.p1 = point1.getCoords()
        self.p2 = point2.getCoords()
        self.x = self.p2[0] - self.p1[0]
        self.y = self.p2[1] - self.p1[1]
        if self.x !=0 :
            self.m = self.y/self.x
            self.p = self.p1[1] - self.m * self.p1[0]

    def points(self):
        pts = []
        x = self.x
        y = self.y
        if self.x != 0 and self.m != 0:
            while x >=0 :
                pts.append((self.p1[0] + x, abs(round(self.m * (self.p1[0] + x) + self.p))))
                x -= 1
        if self.x == 0 :
            while y >= 0:
                pts.append((self.p1[0], y + self.p1[1]))
                y -= 1

        if self.p1[1] == self.p2[1]:
            while x >=0 :
                pts.append((self.p1[0]+x, self.p1[1]))
                x -= 1

        return pts

class Cursor():
    def __init__(self, width, height, points):
        self.x = width
        self.y = height
        self.points = points

    def update(self, points):
        self.points = points

    def run(self):
        string = ""
        x=0
        y=self.y
        while y >= 0:
            while x<=self.x:
                pointed = False
                for point in self.points :
                    if point[0] == x and point[1] == y and pointed == False:
                        pointed = True
                        string += "#"
                if not pointed :
                    string += " "
                x +=1
            y -= 1
            x= 0
            string += "\n"
        return string

class Cube():
    def __init__(self, x=0, y=0, scaleX=1, scaleY=1, rotX=0, rotY=0):
        self.points = [Point(x,y), Point(x+scaleX, y), Point(x+scaleX, y), Point(x,y), Point(x, y+scaleY), Point(x+scaleX, y+scaleY), Point(x+scaleX, y+scaleY), Point(x, y+scaleY)]
        self.rotX(rotX)
        self.rotY(rotY)

    def Lines(self):
        p = self.points
        self.lines = [Line(p[0],p[1]),Line(p[1],p[2]),Line(p[3],p[2]),Line(p[0],p[3]),Line(p[0],p[4]),Line(p[1],p[5]),Line(p[2],p[6]),Line(p[3],p[7]),Line(p[4],p[5]),Line(p[5],p[6]),Line(p[7],p[6]),Line(p[4],p[7])]
        self.result = []
        for line in self.lines:
            self.result += line.points()
        return self.result

    def rotX(self,rot):
        self.points[3].move(rot,0)
        self.points[2].move(rot,0)
        self.points[7].move(rot,0)
        self.points[6].move(rot,0)

    def rotY(self,rot):
        self.points[3].move(0,rot)
        self.points[2].move(0,rot)
        self.points[7].move(0,rot)
        self.points[6].move(0,rot)

    def getRotX(self):
        return self.points[3].getCoords()[0] - self.points[0].getCoords()[0]

    def getRotY(self):
        return self.points[3].getCoords()[1] - self.points[0].getCoords()[1]

def update():
    cursor.update(c.Lines())
    dtring = cursor.run()
    os.system('clear')
    print(dtring)
if __name__ == "__main__":
    c = Cube(2,2,24,24,5,5)
    cursor = Cursor(100,100, c.Lines())
    print(cursor.run())
    while True :
        time.sleep(0.1)
        if c.getRotX() < 24 :
            c.rotX(2)
        else :
            c.rotX(-24)
            if c.getRotY() < 24 :
                c.rotY(1)
            else :
                c.rotY(-24)
        update()  
    
