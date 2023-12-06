import pyvisa

rm1 = pyvisa.ResourceManager()
print(rm1.list_resources())

laser = rm1.open_resource('GPIB0::10::INSTR')
laser.write_termination = '\r'
laser.read_termination = '\r'
laser.baud_rate = 9600
laser.data_bits = 8

response = laser.query('*IDN?', delay=1)
print(response)
laser.close()

rm2= pyvisa.ResourceManager('@py')
powermeter = rm2.open_resource('USB0::4883::32888::P0001012::0::INSTR')
powermeter.write_termination = '\r'
powermeter.read_termination = '\r'
print(powermeter.query('*IDN?'))
