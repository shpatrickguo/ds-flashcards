---
name: Determine Optimal Sample Size for an A/B Test
tags: statistics, ab-test
---

## Q: How to Determine Optimal Sample Size for an A/B Test (Technical)

The optimal sample size in an A/B test depends primarily on:

- The **minimum detectable effect (δ)**: the smallest difference between groups A and B considered meaningful.
- The **statistical power (1 - β)**: probability of detecting a true effect, commonly set to 80%.
- The **significance level (α)**: the threshold for false positive rate, often 5%.

### Sample Size Formula (Equal Variances, Two-Sample Test)

\[
n = \frac{(Z_{\alpha/2} + Z_\beta)^2 \times (\sigma_A^2 + \sigma_B^2)}{\delta^2}
\]

Where:

- \( n \) = sample size per group
- \( Z_{\alpha/2} \) = critical value for significance level (e.g., 1.96 for α=0.05)
- \( Z_\beta \) = critical value for power (e.g., 0.84 for 80% power)
- \( \sigma_A^2 \), \( \sigma_B^2 \) = variances of groups A and B
- \( \delta \) = minimum detectable effect size

## How to Determine Optimal Sample Size for an A/B Test (Non-Technical)

To know how many people you need in each group of your A/B test, consider three things:

- The **smallest improvement** you want to spot between the groups.
- The **chance** you want to have of noticing a real difference (usually 80%).
- How sure you want to be that differences you see aren’t just luck (common is 95% confidence).

### What This Means

If you want to be confident your test results are real (not a fluke), you need enough people in each group. The smaller the improvement you want to detect, the more people you need. For example, spotting a tiny difference needs more participants than spotting a big jump.

--
