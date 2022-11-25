import random
from tkinter import Y
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw_points(x, y):
    glPointSize(6)
    glColor3f(214 / 255, 125 / 255, 20/ 255)
    glBegin(GL_POINTS)
    glVertex2f(x,y) 
    glEnd()

def DrawLine(x1,y1,x2,y2):
    zone=FindZone(x1,y1,x2,y2)
    x1,y1=ConvertToZone0(x1,y1,zone)
    x2,y2=ConvertToZone0(x2,y2,zone)
    dx = x2-x1
    dy = y2-y1
    d = 2*dy-dx
    incE =2*dy
    incNE=2*(dy-dx)
    x=x1
    y=y1
    while (x<=x2): 
        p,q=OriginalZone(x,y,zone)
        draw_points(p,q)
        if d>0:
            d+=incNE
            y+=1
        else:
            d+=incE
        
def FindZone(x1,y1,x2,y2):
    zone=0
    dx=x2-x1
    dy=y2-y1
    if abs(dx)>=abs(dy):
        if dx>=0 and dy>=0:
            zone=0
        elif dx<0 and dy>=0:
            zone=3
        elif dx<0 and dy<0:
            zone=4
        elif dx>=0 and dy<0:
            zone=7
    else:
        if dx>=0 and dy>=0:
            zone=1
        elif dx<0 and dy>=0:
            zone=2
        elif dx<0 and dy<0:
            zone=5
        elif dx>=0 and dy<0:
            zone=6
    return zone


def ConvertToZone0(x1,y1,zone): 
    if zone==0:
        x1=x1
        y1=y1
    elif zone==1:
        x1=y1
        y1=x1
    elif zone==2:
        x1=y1
        y1=-x1
    elif zone==3:
        x1=-x1
        y1=y1
    elif zone==4:
        x1=-x1
        y1=-y1
    elif zone==5:
        x1=-y1
        y1=-x1
    elif zone==6:
        x1=-y1
        y1=x1
    elif zone==7:
        x1=x1
        y1=-y1
    return x1,y1

def OriginalZone(x1,y1,zone):
    if zone==0:
        x1=x1
        y1=y1
    elif zone==1:
        x1=y1
        y1=x1
    elif zone==2:
        x1=-y1
        y1=x1
    elif zone==3:
        x1=-x1
        y1=y1
    elif zone==4:
        x1=-x1
        y1=-y1
    elif zone==5:
        x1=-y1
        y1=-x1
    elif zone==6:
        x1=y1
        y1=-x1
    elif zone==7:
        x1=x1
        y1=-y1
    return x1,y1

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate() 
    DrawLine(92,373,185,373)
    DrawLine(92,373,92,285)
    DrawLine(92,285,185,285)
    DrawLine(185,373,185,136)

    DrawLine(254,373,346,373)
    DrawLine(254,373,254,285)
    DrawLine(254,285,346,285)
    DrawLine(346,373,346,136)
    # DrawLine(200,300,300,300)
    # DrawLine(300,300,300,250)
    # DrawLine(200,250,300,250)
    # DrawLine(200,250,200,200)
    # DrawLine(200,200,300,200)
    # DrawLine(400,300,400,260)
    # DrawLine(400,300,500,300)
    # DrawLine(400,260,500,260)
    # DrawLine(500,300,500,200)
    # DrawLine(400,200,500,200)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"ID:20101329") 
glutDisplayFunc(showScreen)
glutMainLoop()