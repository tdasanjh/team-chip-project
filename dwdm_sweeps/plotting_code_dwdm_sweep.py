import pandas as pd
import matplotlib.pyplot as plt
def get_wavlen_and_pow_arrays(data_filepath):
    # to get an array of wavelengths and an array of powers from csv
    # takes in full csv filepath with wavelength in first column and power in second
    #returns a tuple of power and wavelength arrays
    data_analyse=pd.read_csv(data_filepath, header=None)
    data_analyse_array=data_analyse.to_numpy(copy=True)

    wavelengths=data_analyse_array[:,0]
    powers_dBm=data_analyse_array[:,1]
    return (wavelengths,powers_dBm)

sweep_data_filename="dwdm_ch_26_1550_1560 2023-12-14 16-33-18.csv"
wavelength_array,power_array=get_wavlen_and_pow_arrays(sweep_data_filename)

fig1,ax1=plt.subplots()
ax1.plot(wavelength_array,power_array)
ax1.set_xlabel("Wavelength/nm")
ax1.set_ylabel("Power/Watts")
plt.show()