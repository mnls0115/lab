from scipy.stats import ttest_rel

# Define the pre-treatment HM ratios
pre_treatment = [199,184,153,9,84.7,25.5,123,143,65.2,78,49.9,83.3,77.9
]  # List of pre-treatment HM ratios for each patient

# Define the post-treatment HM ratios
post_treatment = [39,30.7,32.4,1.08,19.4,7.03,16,6.73,47,13.4,3,67.6,25.9
]  # List of post-treatment HM ratios for each patient

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