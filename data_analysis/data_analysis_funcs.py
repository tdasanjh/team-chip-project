import scipy.signal
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def dBm_to_mW(powers_dBm):
    #func to convert dBm to mW
    #takes in power in dBm and returns power in mW
    return 10**(powers_dBm/10)
#vectorising the func to convert dBm to mW
vector_dBm_to_mW=np.vectorize(dBm_to_mW)

def get_wavlen_and_pow_arrays(data_filepath):
    # to get an array of wavelengths and an array of powers from csv
    # takes in full csv filepath with wavelength in first column and power in second
    #returns a tuple of power and wavelength arrays
    data_analyse=pd.read_csv(data_filepath, header=None)
    data_analyse_array=data_analyse.to_numpy(copy=True)

    wavelengths=data_analyse_array[:,0]
    powers_dBm=data_analyse_array[:,1]
    return (wavelengths,powers_dBm)

def plot_visualise(wavelengths, powers, full_range=True, start_index=0, stop_index=-1):
    # to plot data or a selection of data
    #takes in wavelengths and powers arrays, True or False for full_range
    #depending on whether you want to plot the full_range and the start and stop index of the arrays
    #you want to plot the selected range from if wish to select the range
    #gives out the plots
    if full_range==True:
        plt.plot(wavelengths,powers)
        plt.show()
    if full_range==False:
        plt.plot(wavelengths[start_index:stop_index],powers[start_index:stop_index])
        plt.show()
    return
    
def give_peak_locs(wavel_step_size,fsr_approx,promin,dist,wavelengths, powers):
    #to give locations of peaks in scan data based on estimates of prominence and
    #takes in wavelength step size, an approximation of the fsr and a prominence for peaks
    #(to see what is meant by prominence see scipy.signal.peak_prominences documentation)
    #returns in a tuple peak locs, number of peaks, and their corresponding power and wavelength values
    neg_powers=-powers
    search_len=fsr_approx/wavel_step_size
    peaks_info=scipy.signal.find_peaks(neg_powers,distance=dist,prominence=promin, wlen=search_len)
    peaks_array=peaks_info[0]
    num_peaks=len(peaks_array)
    peak_wavelengths=[wavelengths[x] for x in peaks_array]
    peak_powers=[powers[x] for x in peaks_array]
    return (peaks_array, num_peaks,peak_wavelengths,peak_powers)

def calc_fsrs(peak_wavelen_vals):
    #calculates free-spectral ranges from a list of peak wavlengths
    #takes in values of wavelengths at peaks
    #returns an array of free spectral ranges
    fsr_list=[]
    for i in range(0,len(peak_wavelen_vals)-1):
        fsr_list.append(peak_wavelen_vals[i+1]-peak_wavelen_vals[i])
    return np.array(fsr_list)

def fsr_avg_and_error(fsr_vals):
    #calculates mean fsr and standard error from list of fsrs
    #takes in a list of fsrs
    #returns mean fsr with standard error.
    mean_fsr=np.mean(fsr_vals)
    std_error=np.std(fsr_vals,ddof=1)/np.sqrt(len(fsr_vals))
    return (mean_fsr,std_error)

def gc_subtracted_spectrum(gc_filepath,structure_filepath):
    #subtracts power spectrum of a grating coupler from that of the structure given
    #takes in filepaths for a grating coupler and other structure csv of power vs wavelength
    #WARNING only works if wavelength ranges and step sizes are the same for both structures
    #returns array of power_dBm_structure-power_dBm_grating_coupler and the array of the structure's wavlengths
    gc_wavelengths,gc_powers=get_wavlen_and_pow_arrays(gc_filepath)
    struc_wavelengths, struc_powers=get_wavlen_and_pow_arrays(structure_filepath)
    subtr_powers=struc_powers-gc_powers
    return (struc_wavelengths,subtr_powers)

def get_peak_FWHM(wavel_step_size,fsr_approx,promin,dist,wavelengths, powers):
    """
    function that gives peak FWHM, and data for visualsing FWHM
    takes in wavelength step size, approx fsr prominence, distance, wavelengths, powers
    returns peak widths, the height at which the peak width was found, and the interpolated 
    left and right wavlength positions of where the peak with was found on the signal.
    """   
    neg_powers=-powers
    search_len=fsr_approx/wavel_step_size
    peak_loc_info=give_peak_locs(wavel_step_size,fsr_approx,promin,dist,wavelengths,powers)
    peak_widths_info=scipy.signal.peak_widths(neg_powers,peak_loc_info[0],rel_height=0.5,wlen=search_len)
    peak_w_array=peak_widths_info[0]
    peak_w_array=peak_w_array*wavel_step_size
    peak_width_heights=-peak_widths_info[1]
    peak_width_left=peak_widths_info[2]*wavel_step_size+wavelengths[0]
    peak_width_right=peak_widths_info[3]*wavel_step_size+wavelengths[0]
    return (peak_w_array,peak_width_heights,peak_width_left,peak_width_right)

def plot_lines_FWHM(peak_width_heights,peak_width_left,peak_width_right,wavelengths,powers):
    plt.plot(wavelengths,powers)
    plt.hlines(peak_width_heights,peak_width_left,peak_width_right,color="red")
    plt.show()
    return

def calc_Q3overR2(Q,Q_error,R,R_error):
    """
    This function finds Q^3/R^2 and it's associated error.
    Takes in Q and its error, and R and its error.
    Returns Q^3/R^2 followed by its associated error.
    """
    ans=Q**3/R**2
    ans_uncertainty=ans*np.sqrt((3*(Q_error/Q))**2+(2*(R_error/R))**2)
    return (ans,ans_uncertainty)
