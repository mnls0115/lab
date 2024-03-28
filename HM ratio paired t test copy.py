from scipy.stats import ttest_rel

# Define the pre-treatment HM ratios
pre_treatment = [122.1,179,219.5,10.75,115.85,44.3,97.45,113.6,70.2,164.5,44.15,85.95,124.45]  # List of pre-treatment HM ratios for each patient

# Define the post-treatment HM ratios
post_treatment = [22.7,76.85,43.2,3.605,14.7,8.5,4.88,35.265,42.3,16.45,2.8,57.6,31.2]  # List of post-treatment HM ratios for each patient

# Perform the paired t-test
statistic, p_value = ttest_rel(pre_treatment, post_treatment)

print("Paired t-test:")
print(f"T-statistic: {statistic}")
print(f"P-value: {p_value}")

#============================================================#

import numpy as np
# Calculate the mean
pre_treatment__mean_value = np.mean(pre_treatment)
post_treatment__mean_value = np.mean(post_treatment)

# Calculate the standard deviation
pre_treatment__std_deviation = np.std(pre_treatment)
post_treatment__std_deviation = np.std(post_treatment)

print("Pre treatment Mean:", pre_treatment__mean_value)
print("pre Standard Deviation:", pre_treatment__std_deviation)
print("Post treatment Mean:", post_treatment__mean_value)
print("prost Standard Deviation:", post_treatment__std_deviation)