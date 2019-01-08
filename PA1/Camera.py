class Camera:
	x = 0
	y = 0
	z = 0
	xMin = 0
	xMax = 0
	yMin = 0
	yMax = 0
	viewDistance = 0
	resolutionX = 0
	resolutionY = 0
	def __init__(self, _x, _y, _z, _xMin, _xMax, _yMin, _yMax, _vd, _resolutionX, _resolutionY):
		self.x = _x
		self.y = _y
		self.z = _z
		self.xMin = _xMin
		self.xMax = _xMax
		self.yMin = _yMin
		self.yMax = _yMax
		self.vd = _vd
		self.resolutionX = _resolutionX
		self.resolutionY = _resolutionY
