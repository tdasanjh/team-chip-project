import pandas as pd

file_path = "C:/Users/IT086179/Desktop/Team_Chip_1_2023/ltphotonics_Freddie_6Dec/team-chip-project/wavelength_sweeps/sg_rr_100_025 2023-12-11 14-23-14.csv"
transmission_data = pd.read_csv(file_path)
transmission_data.plot()



