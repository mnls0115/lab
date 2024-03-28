from scipy.stats import ttest_rel

# Define the pre-treatment HM ratios
pre_treatment_MMTsum= [23.5,51.5,22,40.5,12,32.5,55.5,31,54,27,29.5]  # List of pre-treatment HM ratios for each patient
pre_treatment_MBI= [34,72,7,72,39,98,7,88,0,5]  # List of pre-treatment HM ratios for each patient

# Define the post-treatment HM ratios
post_treatment_MMTsum = [24,53,12,38,12,14,53.5,27,45.5,26,24.5]  # List of post-treatment HM ratios for each patient
post_treatment_MBI = [37,92,5,76,39,98,7,90,2,18]  # List of post-treatment HM ratios for each patient

# Perform the paired t-test
statistic_MMT, p_value_MMT = ttest_rel(pre_treatment_MMTsum, post_treatment_MMTsum)
statistic_MBI, p_value_MbI = ttest_rel(pre_treatment_MBI, post_treatment_MBI)

print("Paired t-test (MMT):")
print(f"T-statistic: {statistic_MMT}")
print(f"P-value: {p_value_MMT}")

print("Paired t-test (MBI):")
print(f"T-statistic: {statistic_MBI}")
print(f"P-value: {p_value_MbI}")

#============================================================#

import numpy as np

# Calculate the mean
pre_treatment__mean_value_MMT = np.mean(pre_treatment_MMTsum)
post_treatment__mean_value_MMT = np.mean(post_treatment_MMTsum)
# Calculate the mean
pre_treatment__mean_value_MBI = np.mean(pre_treatment_MBI)
post_treatment__mean_value_MBI = np.mean(post_treatment_MBI)

# Calculate the standard deviation
pre_treatment__std_deviation_MMT = np.std(pre_treatment_MMTsum)
post_treatment__std_deviation_MMT = np.std(post_treatment_MMTsum)
# Calculate the standard deviation
pre_treatment__std_deviation_MBI = np.std(pre_treatment_MBI)
post_treatment__std_deviation_MBI = np.std(post_treatment_MBI)

print("Pre-Post MMT")
print("Pre treatment Mean:", pre_treatment__mean_value_MMT)
print("pre Standard Deviation:", pre_treatment__std_deviation_MMT)
print("Post treatment Mean:", post_treatment__mean_value_MMT)
print("prost Standard Deviation:", post_treatment__std_deviation_MMT)

print("Pre-Post MBI")
print("Pre treatment Mean:", pre_treatment__mean_value_MBI)
print("pre Standard Deviation:", pre_treatment__std_deviation_MBI)
print("Post treatment Mean:", post_treatment__mean_value_MBI)
print("prost Standard Deviation:", post_treatment__std_deviation_MBI)