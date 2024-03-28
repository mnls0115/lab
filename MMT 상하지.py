from scipy.stats import ttest_rel

# Define the pre-treatment HM ratios
pre_treatment_MMTsum상= [2.25,5,2.16666666666667,4,1,3.91666666666667,5,2.5,4.5,2.5,2.75
]  # List of pre-treatment HM ratios for each patient
pre_treatment_MMTsum하= [1.66666666666667,3.58333333333333,1.5,2.75,1,1.5,4.25,2.66666666666667,4.5,2,2.16666666666667
]  # List of pre-treatment HM ratios for each patient

# Define the post-treatment HM ratios
post_treatment_MMTsum상 = [2.33333333333333,5,1,4,1,2,5,2.66666666666667,3.75,2.33333333333333,2.25
]  # List of post-treatment HM ratios for each patient
post_treatment_MMTsum하 = [1.66666666666667,3.83333333333333,1,2.33333333333333,1,1.66666666666667,3.91666666666667,1.83333333333333,3.83333333333333,2,1.83333333333333
]  # List of post-treatment HM ratios for each patient

# Perform the paired t-test
statistic_MMT, p_value_MMT = ttest_rel(pre_treatment_MMTsum상, post_treatment_MMTsum상)
statistic_MBI, p_value_MbI = ttest_rel(pre_treatment_MMTsum하, post_treatment_MMTsum하)

print("Paired t-test (MMT):")
print(f"T-statistic: {statistic_MMT}")
print(f"P-value: {p_value_MMT}")

print("Paired t-test (MBI):")
print(f"T-statistic: {statistic_MBI}")
print(f"P-value: {p_value_MbI}")

#============================================================#

import numpy as np

# Calculate the mean
pre_treatment__mean_value_MMT = np.mean(pre_treatment_MMTsum상)
post_treatment__mean_value_MMT = np.mean(post_treatment_MMTsum상)
# Calculate the mean
pre_treatment__mean_value_MBI = np.mean(pre_treatment_MMTsum하)
post_treatment__mean_value_MBI = np.mean(post_treatment_MMTsum하)

# Calculate the standard deviation
pre_treatment__std_deviation_MMT = np.std(pre_treatment_MMTsum상)
post_treatment__std_deviation_MMT = np.std(post_treatment_MMTsum상)
# Calculate the standard deviation
pre_treatment__std_deviation_MBI = np.std(pre_treatment_MMTsum하)
post_treatment__std_deviation_MBI = np.std(post_treatment_MMTsum하)

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