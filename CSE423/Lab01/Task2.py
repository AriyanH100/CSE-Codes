from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points():
    glPointSize(4) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glColor3f(245.0/255,135.0/255,66.0/255)

    glVertex2f(420,250)  
    glEnd()

def draw_lines():
    glBegin(GL_LINES)
    glColor3f(245.0/255, 66.0/255, 242.0/255)

    glVertex2f(300, 200)   
    glVertex2f(300, 400)  

    glVertex2f(300, 400)   
    glVertex2f(500, 400)  

    glVertex2f(500, 400)   
    glVertex2f(500, 200)  

    glVertex2f(500, 200)   
    glVertex2f(300, 200)  

#-------------------------------------------------------#
    glColor3f(102.0/255,25.0/255,18.0/255)
    
    glVertex2f(300, 400)   
    glVertex2f(400, 500)   

    glVertex2f(400, 500)   
    glVertex2f(500, 400)   

# -------------------------------------------------------#
    glColor3f(66.0/255,224.0/255,245.0/255)
    
    glVertex2f(320, 330)   
    glVertex2f(320, 380)   

    glVertex2f(320, 380)   
    glVertex2f(370, 380)   

    glVertex2f(370, 380)   
    glVertex2f(370, 330)   

    glVertex2f(370, 330)   
    glVertex2f(320, 330)   

# -------------------------------------------------------#

    glVertex2f(480, 330)   
    glVertex2f(480, 380)   

    glVertex2f(480, 380)   
    glVertex2f(430, 380)   

    glVertex2f(430, 380)   
    glVertex2f(430, 330)   

    glVertex2f(430, 330)   
    glVertex2f(480, 330)   

# -------------------------------------------------------#
    glColor3f(245.0/255,224.0/255,66.0/255)

    glVertex2f(370, 200)   
    glVertex2f(370, 300)  

    glVertex2f(370, 300)   
    glVertex2f(430, 300)  

    glVertex2f(430, 300)   
    glVertex2f(430, 200)  

    glVertex2f(430, 200)   
    glVertex2f(370, 200)  

    glEnd()

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
    
    draw_lines()
    draw_points()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800) 
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") 
glutDisplayFunc(showScreen)

glutMainLoop()

