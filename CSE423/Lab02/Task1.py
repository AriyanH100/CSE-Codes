from tkinter import Y
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x,y):
    glPointSize(10) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y)  
    glEnd()

def findZone(x1,y1,x2,y2):
    zone=0
    dx=x2-x1
    dy=y2-y1
    if abs(dx)>=abs(dy):
        if dx>=0 and dy>=0:
            zone=0
        if dx<0 and dy>=0:
            zone=3
        if dx<0 and dy<0:
            zone=4
        if dx>=0 and dy<0:
            zone=7
    else:
        if dx>=0 and dy>=0:
            zone=1
        if dx<0 and dy>=0:
            zone=2
        if dx<0 and dy<0:
            zone=5
        if dx>=0 and dy<0:
            zone=6
    return zone

def convertToZone0(x,y,zone):
    if zone==0:
        a=x
        b=y
        return a,b
    elif zone==1:
        a=y
        b=x
        return a,b
    elif zone==2:
        a=y
        b=-x
        return a,b
    elif zone==3:
        a=-x
        b=y
        return a,b
    elif zone==4:
        a=-x
        b=-y
        return a,b
    elif zone==5:
        a=-y
        b=-x
        return a,b
    elif zone==6:
        a=-y
        b=x
        return a,b
    elif zone==7:
        a=x
        b=-y
        return a,b

def convertBack(x,y,zone):
    if zone==0:
        a=x
        b=y
        return a,b
    elif zone==1:
        a=y
        b=x
        return a,b
    elif zone==2:
        a=-y
        b=x
        return a,b
    elif zone==3:
        a=-x
        b=y
        return a,b
    elif zone==4:
        a=-x
        b=-y
        return a,b
    elif zone==5:
        a=-y
        b=-x
        return a,b
    elif zone==6:
        a=y
        b=-x
        return a,b
    elif zone==7:
        a=x
        b=-y
        return a,b


def drawline(x1,y1,x2,y2):
    zone=findZone(x1,y1,x2,y2)
    x1,y1=convertToZone0(x1,y1,zone)
    x2,y2=convertToZone0(x2,y2,zone)
    dx=x2-x1
    dy=y2-y1
    d=2*dy-dx
    incE=2*dy
    incNE=2*(dy-dx)
    x=x1
    y=y1
    while True:
        X,Y=convertBack(x,y,zone)
        draw_points(X,Y)
        if d>0:
            d+=incNE
            y+=1
        else:
            d+=incE
        x+=1
        if x==x2 and y==y2:
            break



def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 1.0) #konokichur color set (RGB)
    #call the draw methods here
    drawline(92,373,185,373)
    drawline(92,373,92,285)
    drawline(92,285,185,285)
    drawline(185,373,185,136)

    drawline(254,373,346,373)
    drawline(254,373,254,285)
    drawline(254,285,346,285)
    drawline(346,373,346,136)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()

