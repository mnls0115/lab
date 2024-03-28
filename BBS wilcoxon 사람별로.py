from scipy.stats import wilcoxon

# Define the pre-treatment MAS grades
pre_treatment = [4,47,24,3,54,41,3]  # List of pre-treatment MAS grades for each patient

# Define the post-treatment MAS grades
post_treatment = [2,52,43,4,52,32,2]  # List of post-treatment MAS grades for each patient

# Perform the Wilcoxon signed-rank test
statistic, p_value = wilcoxon(pre_treatment, post_treatment)

print("Wilcoxon Signed-Rank Test:")
print(f"Test Statistic: {statistic}")
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