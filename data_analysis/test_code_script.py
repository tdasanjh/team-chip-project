import data_analysis_funcs as daf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal

"""
# testing dBm to mW func by using calculator (just doing /10 bit in head)
A=[-15.5,-12.23,-21.6,-9.8]
print(daf.vector_dBm_to_mW(A))
#check passed
"""
"""
xs,ys=daf.get_wavlen_and_pow_arrays("C:\\Users\\TamCoding\\Documents\\Team_project\\shared_git_repo\\team-chip-project\\data_analysis\\dummy_data.csv")
print(xs)
print(ys)
#works but misses off first row in CSV file, so added header=None to original func.
print(len(xs))
print(len(ys))
"""
"""
daf.plot_visualise(xs,ys)
daf.plot_visualise(xs,ys,full_range=False,start_index=5,stop_index=10)
#seems to work
"""
"""
xs,ys=daf.get_wavlen_and_pow_arrays("C:\\Users\\TamCoding\\Documents\\Team_project\\shared_git_repo\\team-chip-project\\data_analysis\\dummy_data_2.csv")
peak_locs, n_peaks, peak_xs, peak_ys=daf.give_peak_locs(0.2,6,0.6,15,xs,ys)
print(peak_locs)
print(n_peaks)
print(peak_xs)
print(peak_ys)
print(xs)
print(ys)
plt.plot(xs,ys)
plt.scatter(peak_xs,peak_ys)
plt.show()
#seems to work when tested in this way although I know signal is not noisy
"""
"""
# test calc fsrs on a dummy list and also the fsr mean and errors calc used excel sheet to test them, worked
fsr_list=[1.1,1.2,1.35,1.46,1.79]
fsr_vals=daf.calc_fsrs(fsr_list)
print(daf.calc_fsrs(fsr_list))
print(daf.fsr_avg_and_error(fsr_vals))
"""
"""
#not going to bother testing subtracted spectrum plot code, as don't think it will be used.
#working out how to use peak_widths
xs=np.linspace(0,2*np.pi,101)
ys=np.sin(8*xs)
plt.plot(xs,ys)
plt.show()
peaks_data=scipy.signal.find_peaks(ys,prominence=0.5, wlen=25)
peak_locs=peaks_data[0]
peak_widths_info=scipy.signal.peak_widths(ys,peak_locs,rel_height=0.5,wlen=25)
peak_widths_heights=peak_widths_info[1]
peak_widths_left_pos=peak_widths_info[2]
peak_widths_right_pos=peak_widths_info[3]
print(peak_widths_info)
print(peak_widths_heights)
print(peak_widths_left_pos)
print(peak_widths_right_pos)
plt.plot(xs,ys)
plt.hlines(peak_widths_heights,peak_widths_left_pos*(2*np.pi/100),peak_widths_right_pos*(2*np.pi/100))
plt.show()
"""
#testing new FWHM code on some dummy data to see if it does what I expect:
#going to use arrays that I just generate as assume that will be fine
wvlen_peak_search=np.linspace(2*np.pi,4*np.pi,101)
wvlen_step_size=2*np.pi/100
approx_fsr=2*(np.pi/8)
promin_use=0.4
#dist_use=(approx_fsr/2)/wvlen_step_size
dist_use=1
power_peak_search=-np.sin(8*wvlen_peak_search)
plt.plot(wvlen_peak_search,power_peak_search)
plt.show()
peak_width_data=daf.get_peak_FWHM(wvlen_step_size,approx_fsr,promin_use,dist_use,wvlen_peak_search,power_peak_search)
peak_widths=peak_width_data[0]
print(peak_widths)
peak_width_heights=peak_width_data[1]
peak_width_lefts=peak_width_data[2]
peak_width_rights=peak_width_data[3]
print(peak_width_rights)
print(peak_width_lefts)
print(peak_width_heights)
daf.plot_lines_FWHM(peak_width_heights,peak_width_lefts,peak_width_rights,wvlen_peak_search,power_peak_search)
mean_FWHM,FWHM_error=daf.fsr_avg_and_error(peak_widths)
print(mean_FWHM)
print(FWHM_error)
