from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
from HalfLine import HalfLine
from Camera import Camera
from Plane import Plane
from Ball import Ball
import Shader
import random

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

cam = Camera(0, 0, 0, -0.1, 0.1, -0.1, 0.1, -0.1, 512, 512)
plane = Plane(-2, 0, [1,1,1], [0,0,0], [0.2,0.2,0.2])
ball1 = Ball(-4,0,-7,1,0,[1,0,0],[0,0,0],[0.2,0,0])
ball2 = Ball(0,0,-7,2,32,[0,0.5,0],[0.5,0.5,0.5],[0,0.2,0])
ball3 = Ball(4,0,-7,1,0,[0,0,1],[0,0,0],[0,0,0.2])
ballList = [ball1, ball2, ball3]
ballList2 = [ball1]

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(400, 400)
	glutCreateWindow(name)
	glutDisplayFunc(test)
	glutMainLoop()
	return

def anti(i, j):
	color = [0,0,0]
	xLocation = startPlaneX+i*(planeDis)
	yLocation = startPlaneY+j*(planeDis)
	pixel = [xLocation, yLocation, -0.1]
	for t in range(numberOfSample):
		xTemp = xLocation + ((random.random()*64)-32)*antialiasingInterval
		yTemp = yLocation + ((random.random()*64)-32)*antialiasingInterval
		line = HalfLine(cam.x, cam.y, cam.z, xTemp-cam.x, yTemp-cam.y, pixel[2]-cam.z)
		colorTemp = getColor(cam, line, ball1, ball2, ball3, plane, ballList, ballList2)
		color[0] = color[0] + colorTemp[0]
		color[1] = color[1] + colorTemp[1]
		color[2] = color[2] + colorTemp[2]
	color[0] = color[0]/numberOfSample
	color[1] = color[1]/numberOfSample
	color[2] = color[2]/numberOfSample
	return color


def getColor(cam, line, ball1, ball2, ball3, plane, ballList, ballList2):
	if(ball1.isIntersected(cam,line)):
		point = ball1.getPoint(cam,line)
		color = Shader.shader2(cam, lightSource, lightIntensity, ball1, line)
	elif(ball2.isIntersected(cam,line)):
		point = ball2.getPoint(cam,line)
		color = Shader.shader3(cam, lightSource, lightIntensity, ball2, line, ballList2)
	elif(ball3.isIntersected(cam,line)):
		point = ball3.getPoint(cam,line)
		color = Shader.shader3(cam, lightSource, lightIntensity, ball3, line, ballList)
	elif(plane.isIntersected(cam,line)):
		point = plane.getPoint(cam,line)
		color = Shader.shader3(cam, lightSource, lightIntensity, plane, line, ballList)
	else:
		color = [0,0,0]

	return color

def test():
	glClear(GL_COLOR_BUFFER_BIT)
	glPointSize(pointSize)
	for i in range(cam.resolutionX):#cam.resolutionX
		print (i)
		for j in range(cam.resolutionX):
			color = anti(i, j)
			glBegin(GL_POINTS)
			glVertex2f(startImageX+i*imageDis, startImageY+j*imageDis)
			glColor3f(color[0], color[1], color[2])
			glEnd()
	glFlush()

if __name__ == '__main__': main()