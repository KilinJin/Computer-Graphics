import math
from Ball import Ball
from Camera import Camera
from HalfLine import HalfLine
def shader(camera, light, point, kd, ks, ka, lightIntensity, specPower):
	ans = [0,0,0]
	normal = [0,1,0]
	lightRayTemp = [light[0]-point[0], light[1]-point[1], light[2]-point[2]]
	lrLength = math.sqrt(lightRayTemp[0]*lightRayTemp[0] + lightRayTemp[1]*lightRayTemp[1] 
		+ lightRayTemp[2]*lightRayTemp[2])
	lightRay = [lightRayTemp[0]/lrLength, lightRayTemp[1]/lrLength, lightRayTemp[2]/lrLength]

	difuse = normal[0]*lightRay[0]+normal[1]*lightRay[1]+normal[2]*lightRay[2]

	eyeRay = [camera.x-point[0], camera.y-point[1], camera.z-point[2]]
	hTemp = [lightRay[0]+eyeRay[0], lightRay[1]+eyeRay[1], lightRay[2]+eyeRay[2]]
	hLength = math.sqrt(hTemp[0]*hTemp[0] + hTemp[1]*hTemp[1] + hTemp[2]*hTemp[2])
	h = [hTemp[0]/hLength, hTemp[1]/hLength, hTemp[2]/hLength]
	specular = h[0]*normal[0] + h[1]*normal[1] + h[2]*normal[2]

	if(difuse>0):
		ans[0] += kd[0]*lightIntensity*difuse
		ans[1] += kd[1]*lightIntensity*difuse
		ans[2] += kd[2]*lightIntensity*difuse
	if(specular>0):
		ans[0] += ks[0]*lightIntensity*(specular**specPower)
		ans[1] += ks[1]*lightIntensity*(specular**specPower)
		ans[2] += ks[2]*lightIntensity*(specular**specPower)
	ans[0] += ka[0]*lightIntensity
	ans[1] += ka[1]*lightIntensity
	ans[2] += ka[2]*lightIntensity
	return ans

def shader2(camera, light, lightIntensity, object, eyeRay):
	ans = [0,0,0]
	normal = [0,1,0]
	point = object.getPoint(camera,eyeRay)
	if(isinstance(object, Ball)):
		normal[0] = (point[0]-object.x)/object.radius
		normal[1] = (point[1]-object.y)/object.radius
		normal[2] = (point[2]-object.z)/object.radius
	kd = object.kd
	ks = object.ks
	ka = object.ka
	specPower = object.specPower
	lightRayTemp = [light[0]-point[0], light[1]-point[1], light[2]-point[2]]
	lrLength = math.sqrt(lightRayTemp[0]*lightRayTemp[0] + lightRayTemp[1]*lightRayTemp[1] 
		+ lightRayTemp[2]*lightRayTemp[2])
	lightRay = [lightRayTemp[0]/lrLength, lightRayTemp[1]/lrLength, lightRayTemp[2]/lrLength]

	difuse = normal[0]*lightRay[0]+normal[1]*lightRay[1]+normal[2]*lightRay[2]

	eyeRay = [camera.x-point[0], camera.y-point[1], camera.z-point[2]]
	hTemp = [lightRay[0]+eyeRay[0], lightRay[1]+eyeRay[1], lightRay[2]+eyeRay[2]]
	hLength = math.sqrt(hTemp[0]*hTemp[0] + hTemp[1]*hTemp[1] + hTemp[2]*hTemp[2])
	h = [hTemp[0]/hLength, hTemp[1]/hLength, hTemp[2]/hLength]
	specular = h[0]*normal[0] + h[1]*normal[1] + h[2]*normal[2]

	if(difuse>0):
		ans[0] += kd[0]*lightIntensity*difuse
		ans[1] += kd[1]*lightIntensity*difuse
		ans[2] += kd[2]*lightIntensity*difuse
	if(specular>0):
		ans[0] += ks[0]*lightIntensity*(specular**specPower)
		ans[1] += ks[1]*lightIntensity*(specular**specPower)
		ans[2] += ks[2]*lightIntensity*(specular**specPower)
	ans[0] += ka[0]*2
	ans[1] += ka[1]*2
	ans[2] += ka[2]*2
	return ans


def shader3(camera, light, lightIntensity, object, eyeRay, ballList):
	ans = [0,0,0]
	normal = [0,1,0]
	point = object.getPoint(camera,eyeRay)
	if(isinstance(object, Ball)):
		normal[0] = (point[0]-object.x)/object.radius
		normal[1] = (point[1]-object.y)/object.radius
		normal[2] = (point[2]-object.z)/object.radius
	kd = object.kd
	ks = object.ks
	ka = object.ka
	specPower = object.specPower
	lightRayTemp = [light[0]-point[0], light[1]-point[1], light[2]-point[2]]
	lrLength = math.sqrt(lightRayTemp[0]*lightRayTemp[0] + lightRayTemp[1]*lightRayTemp[1] 
		+ lightRayTemp[2]*lightRayTemp[2])
	lightRay = [lightRayTemp[0]/lrLength, lightRayTemp[1]/lrLength, lightRayTemp[2]/lrLength]

	difuse = normal[0]*lightRay[0]+normal[1]*lightRay[1]+normal[2]*lightRay[2]

	eyeRay = [camera.x-point[0], camera.y-point[1], camera.z-point[2]]
	eyeRayLength = math.sqrt(eyeRay[0]*eyeRay[0] + eyeRay[1]*eyeRay[1] + eyeRay[2]*eyeRay[2])
	eyeRay = [eyeRay[0]/eyeRayLength, eyeRay[1]/eyeRayLength, eyeRay[2]/eyeRayLength]
	hTemp = [lightRay[0]+eyeRay[0], lightRay[1]+eyeRay[1], lightRay[2]+eyeRay[2]]
	hLength = math.sqrt(hTemp[0]*hTemp[0] + hTemp[1]*hTemp[1] + hTemp[2]*hTemp[2])
	h = [hTemp[0]/hLength, hTemp[1]/hLength, hTemp[2]/hLength]
	specular = h[0]*normal[0] + h[1]*normal[1] + h[2]*normal[2]

	blocked = False
	camm = Camera(point[0], point[1], point[2], 0,0,0,0,0,0,0)
	lightLine = HalfLine(point[0], point[1], point[2], light[0]-point[0], light[1]-point[1], light[2]-point[2])
	for i in range(len(ballList)):
		if(ballList[i].isIntersected(camm, lightLine) and ballList[i] != object):
			blocked = True

	if(difuse>0 and blocked == False):
		ans[0] += kd[0]*lightIntensity*difuse
		ans[1] += kd[1]*lightIntensity*difuse
		ans[2] += kd[2]*lightIntensity*difuse
	if(specular>0 and blocked == False):
		ans[0] += ks[0]*lightIntensity*(specular**specPower)
		ans[1] += ks[1]*lightIntensity*(specular**specPower)
		ans[2] += ks[2]*lightIntensity*(specular**specPower)
	ans[0] += ka[0]*2
	ans[1] += ka[1]*2
	ans[2] += ka[2]*2
	return ans


