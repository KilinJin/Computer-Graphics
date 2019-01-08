import math
class HalfLine:
	startX = 0
	startY = 0
	startZ = 0
	orientX = 0
	orientY = 0
	orientZ = 0

	def __init__(self, sx, sy, sz, ox, oy, oz):
		self.startX = sx
		self.startY = sy
		self.startZ = sz
		self.orientX = ox
		self.orientY = oy
		self.orientZ = oz

	def getLen(self):
		return math.sqrt(self.orientX*self.orientX + self.orientY*self.orientY + self.orientZ*self.orientZ)

	#self to hl, which means self is the longest edge; also assume they share a same starting point
	def getSquareDistance(self, _hl):
		dot = self.orientX*_hl.orientX + self.orientY*_hl.orientY + self.orientZ*_hl.orientZ
		edge0 = dot/_hl.getLen()
		return self.getLen()*self.getLen() - edge0*edge0