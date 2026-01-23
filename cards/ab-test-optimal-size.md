---
name: Determine Optimal Sample Size for an A/B Test
tags: statistics, ab-test
---

## Q: How to determine the optimal sample size for an A/B test?

## Answer (Technical)

The optimal sample size depends on three core inputs:
- Minimum detectable effect (δ): the smallest difference between groups A and B you care about detecting.
- Significance level (α): the acceptable false-positive rate (commonly 0.05 for 95% confidence).
- Statistical power (1 − β): the probability of detecting a true effect (commonly 0.8 or 80%).

For two independent samples with equal variances (continuous outcome), a common formula is:

```n = ((Z_{α/2} + Z_{β})^2 * (σ_A^2 + σ_B^2)) / δ^2```

where `n` is the sample size per group, `Z_{α/2}` and `Z_{β}` are the standard normal critical values for the chosen `α` and `β`, `σ_A^2` and `σ_B^2` are the group variances, and `δ` is the minimum detectable difference in the metric.

For binary outcomes (e.g., conversion rates) you can use a proportions-based approximation:

```n = ((Z_{α/2} * sqrt{2 * p̄ * (1−p̄)} + Z_{β} * sqrt{p_A*(1−p_A) + p_B*(1−p_B)})^2) / (p_A − p_B)^2```

where `p̄ = (p_A + p_B)/2` and `p_A/p_` are the baseline and treatment conversion rates (expressed as decimals).

Practical steps to compute sample size:
1. Choose your baseline rate (or estimate variance) from historical data.
2. Decide the minimum meaningful lift (absolute or relative) you want to detect.
3. Pick α and desired power (e.g., α=0.05, power=0.8).
4. Solve the relevant formula (or use a sample-size calculator or statistical package) to get n per group.

Notes:
- Smaller detectable effects require much larger sample sizes.
- Higher desired power (e.g., 90%) increases required sample size.
- If you plan unequal group sizes, adjust formulas or use software that supports allocation ratios.

## Answer (Non-Technical)

To know how many people you need in each group, you must decide three things:
- The smallest improvement you want to be able to spot.
- How sure you want to be that an observed difference isn’t just random luck (confidence level).
- The chance you want of catching a real improvement when it exists (power).

If you want to be confident your test results are real (not a fluke), you need enough people in each group. The smaller the improvement you want to detect, the more people you need. For example, spotting a 1% improvement on a 10% conversion baseline usually requires many thousands of users per group. Use a sample-size calculator or a short script to plug in your baseline, desired lift, α and power to get an exact number.

## References / Tools
- Many statistics libraries and online calculators (e.g., statsmodels, power.prop_test, G*Power) provide functions to compute these values.
