class Plane:
	y = 0
	specPower = 0
	kd = [0,0,0]
	ks = [0,0,0]
	ka = [0,0,0]

	def __init__(self, _y, _specPower, _kd, _ks, _ka):
		self.y = _y
		self.specPower = _specPower
		self.kd = _kd
		self.ks = _ks
		self.ka = _ka

	def isIntersected(self, camera, hl):
		if (hl.orientY < 0):
			return True
		else:
			return False

	def getPoint(self, camera, hl):
		ans = [0,0,0]
		t = (self.y-hl.startY)/hl.orientY
		ans[0] = hl.startX + t*hl.orientX
		ans[1] = self.y
		ans[2] = hl.startZ + t*hl.orientZ
		return ans