---
name: Explain Adam Optimizer Update Rule
tags: machine-learning, optimizers, deep-learning
---

## Q: How does the Adam optimizer update parameters in one step?

## Answer (Technical)

Adam ("Adaptive Moment Estimation") combines **momentum** (first moment of gradients) with **adaptive step sizes** (second moment of squared gradients), plus **bias correction**.

**Update equations** (per parameter):
```
m_t = β₁ × m_{t-1} + (1 - β₁) × g_t
v_t = β₂ × v_{t-1} + (1 - β₂) × g_t²

m̂_t = m_t / (1 - β₁ᵗ) # bias correction
v̂_t = v_t / (1 - β₂ᵗ)

θ_t = θ_{t-1} - α × m̂_t / (√v̂_t + ε)
```
**Parameters:**
- `g_t`: gradient at time `t`
- `β₁=0.9`, `β₂=0.999`: exponential decay rates
- `α=0.001`: learning rate
- `ε=10⁻⁸`: numerical stability

**Mathematical intuition:** Large-gradient params get smaller effective LR; small-gradient params get larger LR. Bias correction prevents early iterations from being overly conservative.

Adam automatically **customizes step sizes** for each parameter and **smooths noisy gradients**.

**Key components:**
1. **Average direction** (m): smooths updates like momentum
2. **Gradient magnitude** (v): noisy params → smaller steps; confident params → bigger steps
3. **Bias correction**: fixes early training where moment estimates start near zero

**Why it works well:**
- Less hyperparameter tuning than SGD
- Handles sparse/noisy gradients automatically  
- Default choice for most deep learning problems

## Answer (Non-Technical)
You can think of Adam as a smart way for a model to “learn how to learn.” Instead of taking the same size step every time, Adam looks at two things: how consistently a parameter has been changing and how noisy or uncertain those changes are. It then automatically adjusts the pace, slowing down where things are volatile and speeding up where it’s confident progress is real.
