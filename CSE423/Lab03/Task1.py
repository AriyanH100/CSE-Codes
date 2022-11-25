from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def draw_points(x,y):
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def MidpointCircle(r,cx,cy):
    d=1-r
    x=0
    y=r
    Circlepoints(x,y,cx,cy)
    while x<=y:
        if d<0:
            d+=2*x+3
        else:
            d+=2*x-2*y+5
            y-=1
        x+=1
        Circlepoints(x,y,cx,cy)

def Circlepoints(x,y,cx,cy): 
    draw_points(x+cx,y+cy)
    draw_points(y+cx,x+cy)
    draw_points(y+cx,-x+cy)
    draw_points(x+cx,-y+cy)
    draw_points(-x+cx,-y+cy)
    draw_points(-y+cx,-x+cy)
    draw_points(-y+cx,x+cy)
    draw_points(-x+cx,y+cy)

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
    glColor3f(1.0, 1.0, 0.0)
    r=140 #radius of big circle
    MidpointCircle(r,250,250)
    noOfCircles=2
    for i in range(noOfCircles):
        theta=i*((2*math.pi)/noOfCircles)
        a=(r/2)*math.cos(theta)
        b=(r/2)*math.sin(theta)
        MidpointCircle(r/2,250+a,250+b)

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()
