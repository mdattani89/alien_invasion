class Settings():
	"""A class to store all setting for Alien Invasion"""

	def __init__(self):
		"""Initialize the game's settings."""
		#screen settings
		self.screen_width = 600
		self.screen_heigth = 400
		self.bg_color = (230,230,230)
		
		#ship setting
		self.ship_speed_factor = 0.5

		#bullet setting
		self.bullet_speed_factor = .25
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60


