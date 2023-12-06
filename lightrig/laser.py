import pyvisa


class Laser:
	"""
	Class to control OSICS laser.
	"""
	def __init__(self, COM_port, channel):
		self.channel = channel
		rm = pyvisa.ResourceManager()
		self.laser = rm.open_resource(COM_port)
		self.laser.timeout = 20000
		self.laser.read_termination = '\r>'
		self.laser.write_termination = '\r'
		return

	def laser_enable(self):
		# response = self.laser.query(f"CH{self.channel}:ENABLE").strip()
		# if not response == f"CH{self.channel}:OK":
		# 	raise Exception(f"Error: {response}")
		# return
	    self.switch_on()

	def switch_on(self):
		self.laser.write(f"CH{self.channel}:ENABLE")  # .strip()
		# if not response == "CH{:}:OK".format(self.channel):
		# 	raise Exception("Error: {}".format(response))
		# return

	def set_wavelength(self, w):
		self.switch_on()
		self.laser.write(f"CH{self.channel}:L={w}")
		# response = self.laser.query(f"CH{self.channel}:L={w}").strip()
		# if not response == "CH{:}:OK".format(self.channel):
		#	raise Exception("Error: {}".format(response))
		# return
