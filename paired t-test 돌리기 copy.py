from scipy import stats

# Define the pre-treatment HM ratios
pre_treatment = [122.1, 179, 10.75, 44.3, 70.2]

# Define the post-treatment HM ratios
post_treatment = [14.6, 11.65, 4.05, 30.8, 39.2]

# Perform the paired t-test
t_stat, p_value = stats.ttest_rel(pre_treatment, post_treatment)

print(f'T-statistic: {t_stat:.3f}')
print(f'P-value: {p_value:.3f}')