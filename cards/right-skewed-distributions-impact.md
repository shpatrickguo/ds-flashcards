---
name: Right-Skewed Distributions in ML
tags: feature-engineering, model-performance, data-preprocessing
---

## Q: Discuss the implications of a right-skewed distribution and how it might impact the model's performance.

## Answer (Technical)

Right-skewed distributions (long right tail) create several modeling challenges:

**Impacts by model type:**
- **Linear models**: Violate normality assumptions. Outliers dominate gradient updates, leading to biased coefficients and poor generalization.
- **Distance-based models** (KNN, SVM, Neural Networks): Extreme values distort distance calculations, giving rare high-value points excessive influence.
- **Tree-based models** (CatBoost, XGBoost): Robust - splits use thresholds, not distributional assumptions.

**Key problems:**
- Gradient instability during optimization
- Over-emphasis on outliers during training
- Poor performance on typical (non-outlier) cases

**Mitigation strategies:**
- Log transform: np.log1p(x) - compresses right tail
- Square root: np.sqrt(x) - milder compression
- Winsorization: Cap at 95th/99th percentile
- Use tree models - no transformation needed

## Answer (Non-Technical)

Right-skewed data has a few extreme high values that pull the average up. This causes problems for models that assume "normal" data patterns, making them overly focused on rare cases while ignoring typical ones. Tree-based models like CatBoost handle this naturally, but for other models, simple math transformations (like log) usually fix the issue.

## Recommended next steps
1. Check skewness: `df[num_cols].skew()`
2. For tree models: Skip transformation (they're robust)
3. For linear models: Apply `np.log1p()` to skewed features
4. Validate with cross-validation before/after transformation
