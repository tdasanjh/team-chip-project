import data_analysis_funcs as daf
import pandas as pd
import matplotlib.pyplot as plt
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


