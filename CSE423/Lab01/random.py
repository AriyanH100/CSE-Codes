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
    glEnd()

def draw_lines1():
    glBegin(GL_LINES)
    glColor3f(245.0/255, 66.0/255, 242.0/255)
    glVertex2f(300, 400)   
    glVertex2f(500, 400)  
    glEnd()
# def draw_triangles():
#     glBegin(GL_TRIANGLES)
#     glColor3f(106.0/255,55.0/255,0/255)

#     glVertex2f(300, 400)   
#     glVertex2f(400, 600)   
#     glVertex2f(400, 600)   

#     glEnd()

# def draw_quads():
#     glBegin(GL_QUADS)
#     glColor3f(255.0 / 255, 0 / 255, 0 / 255)
#     glVertex2f(100, 400)   
#     glVertex2f(100, 600)  
#     glVertex2f(200, 600)   
#     glVertex2f(200, 400)   
    
#     glEnd()

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
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    draw_lines()
    draw_lines1()
    draw_points()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()

