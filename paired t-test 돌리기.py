from scipy.stats import ttest_rel

# Define the pre-treatment HM ratios
pre_treatment = [199,184,9,25.5,65.2
                 # 39,30.7,1.08,7.03,47
]  # List of pre-treatment HM ratios for each patient

# Define the post-treatment HM ratios
post_treatment = [12.4, 11.2, 4.19, 19, 38.6
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