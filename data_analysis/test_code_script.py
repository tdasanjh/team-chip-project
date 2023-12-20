import data_analysis_funcs as daf
import pandas as pd
"""
# testing dBm to mW func by using calculator (just doing /10 bit in head)
A=[-15.5,-12.23,-21.6,-9.8]
print(daf.vector_dBm_to_mW(A))
#check passed
"""

xs,ys=daf.get_wavlen_and_pow_arrays("C:\\Users\\TamCoding\\Documents\\Team_project\\shared_git_repo\\team-chip-project\\data_analysis\\dummy_data.csv")
print(xs)
print(ys)
#works but misses off first row in CSV file
print(len(xs))
print(len(ys))

# trying instead 
data=pd.read_csv("C:\\Users\\TamCoding\\Documents\\Team_project\\shared_git_repo\\team-chip-project\\data_analysis\\dummy_data.csv",header=None)
data_array=data.to_numpy(copy=True)
xs=data_array[:,0]
ys=data_array[:,1]
print(xs)
print(ys)
print(len(xs))
print(len(ys))