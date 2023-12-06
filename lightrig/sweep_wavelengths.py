"""
Script to run wavelength sweep once manually coupled.
Saves data as a csv file in specified directory.
"""

from pathlib import Path

from laser import Laser
from powermeter import Powermeter
from sweeper import Sweeper


# Wavelength sweep parameters
device_name = "racetrack-01"
start_wavelength = 1550
end_wavelength = 1555
wavelength_step = 0.1

# Instrument parameters
powermeter_serial = 'P0001012'
laser_com_port = 'GPIB0::10::INSTR'
laser_channel = 1
save_path = Path("C:\\Users\\IT086179\Desktop\\Team_Chip_1_2023\\wavelength_sweeps")

# Connect to instruments
laser = Laser(COM_port=laser_com_port, channel=laser_channel)
powermeter = Powermeter(powermeter_serial)

# Run wavelength sweep
sweeper = Sweeper(laser, powermeter)
sweeper.sweep(
    save_path=save_path,
    device_name=device_name,
    start=start_wavelength,
    end=end_wavelength,
    step=wavelength_step,
)
