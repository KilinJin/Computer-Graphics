from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
from HalfLine import HalfLine
from Camera import Camera
from Plane import Plane
from Ball import Ball
import Shader

name = "pa1"
pointSize = 2/512
startImageX = -1 + 1/512
startImageY = -1 + 1/512
imageDis = 2/512
startPlaneX = -0.1+(0.1/512)
startPlaneY = -0.1+(0.1/512)
planeDis = 0.2/512
lightSource = [-4,4,-3]
lightIntensity = 1

numberOfSample = 64
antialiasingInterval = planeDis/numberOfSample

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(400, 400)
	glutCreateWindow(name)
	glutDisplayFunc(test)
	glutMainLoop()
	return

def test():
	cam = Camera(0, 0, 0, -0.1, 0.1, -0.1, 0.1, -0.1, 512, 512)
	plane = Plane(-2, 0, [1,1,1], [0,0,0], [0.2,0.2,0.2])
	ball1 = Ball(-4,0,-7,1,0,[1,0,0],[0,0,0],[0.2,0,0])
	ball2 = Ball(0,0,-7,2,32,[0,0.5,0],[0.5,0.5,0.5],[0,0.2,0])
	ball3 = Ball(4,0,-7,1,0,[0,0,1],[0,0,0],[0,0,0.2])
	ballList = [ball1, ball2, ball3]
	ballList2 = [ball1]
	glClear(GL_COLOR_BUFFER_BIT)
	glPointSize(pointSize)
	for i in range(cam.resolutionX):#cam.resolutionX
		for j in range(cam.resolutionX):
			pixel = [startPlaneX+i*(planeDis), startPlaneY+j*(planeDis), -0.1]
			line = HalfLine(cam.x, cam.y, cam.z, pixel[0]-cam.x, pixel[1]-cam.y, pixel[2]-cam.z)
			if(ball1.isIntersected(cam,line)):
				point = ball1.getPoint(cam,line)
				color = Shader.shader2(cam, lightSource, lightIntensity, ball1, line)
				glBegin(GL_POINTS)
				glVertex2f(startImageX+i*imageDis, startImageY+j*imageDis)
				glColor3f(color[0], color[1], color[2])
				glEnd()
			elif(ball2.isIntersected(cam,line)):
				point = ball2.getPoint(cam,line)
				color = Shader.shader3(cam, lightSource, lightIntensity, ball2, line, ballList2)
				glBegin(GL_POINTS)
				glVertex2f(startImageX+i*imageDis, startImageY+j*imageDis)
				glColor3f(color[0], color[1], color[2])
				glEnd()
			elif(ball3.isIntersected(cam,line)):
				point = ball3.getPoint(cam,line)
				color = Shader.shader3(cam, lightSource, lightIntensity, ball3, line, ballList)
				glBegin(GL_POINTS)
				glVertex2f(startImageX+i*imageDis, startImageY+j*imageDis)
				glColor3f(color[0], color[1], color[2])
				glEnd()
			elif(plane.isIntersected(cam,line)):
				point = plane.getPoint(cam,line)
				color = Shader.shader3(cam, lightSource, lightIntensity, plane, line, ballList)
				glBegin(GL_POINTS)
				glVertex2f(startImageX+i*imageDis, startImageY+j*imageDis)
				glColor3f(color[0], color[1], color[2])
				glEnd()
	glFlush()

if __name__ == '__main__': main()