from HalfLine import HalfLine
import math
class Ball:
	x = 0
	y = 0
	z = 0
	radius = 0
	specPower = 0
	kd = [0,0,0]
	ks = [0,0,0]
	ka = [0,0,0]

	def __init__(self, _x, _y, _z, _radius, _specPower, _kd, _ks, _ka):
		self.x = _x
		self.y = _y
		self.z = _z
		self.radius = _radius
		self.specPower = _specPower
		self.kd = _kd
		self.ks = _ks
		self.ka = _ka

	def isIntersected(self, camera, hl2):
		hl1 = HalfLine(camera.x, camera.y, camera.z, self.x-camera.x, self.y-camera.y, self.z-camera.z)
		squareDis = hl1.getSquareDistance(hl2)
		if(squareDis>self.radius*self.radius):
			return False
		else:
			return True

	def getPoint(self, camera, hl2):
		ans = [0,0,0]
		hl1 = HalfLine(camera.x, camera.y, camera.z, self.x-camera.x, self.y-camera.y, self.z-camera.z)
		longSquareDis = hl1.getLen()**2
		shortSquareDis = hl1.getSquareDistance(hl2)
		midSquareDis = longSquareDis-shortSquareDis
		cutSquareDis = self.radius*self.radius-shortSquareDis
		realDis = math.sqrt(midSquareDis) - math.sqrt(cutSquareDis)
		t = math.sqrt(realDis*realDis/(hl2.orientX**2+hl2.orientY**2+hl2.orientZ**2))
		ans[0] = hl2.startX+hl2.orientX*t
		ans[1] = hl2.startY+hl2.orientY*t
		ans[2] = hl2.startZ+hl2.orientZ*t
		return ans


