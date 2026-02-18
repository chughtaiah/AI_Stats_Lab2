"""
ai_stats_lab.py
AI Mathematical Tools – Probability & Random Variables

Instructions:
- Implement ALL functions.
- Do NOT change function names or signatures.
- Do NOT print inside functions.
- You may use: math, numpy, matplotlib.
"""

import math
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# Part 1 — Probability Foundations
# ============================================================

def probability_union(PA, PB, PAB):
    """
    P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
    """
    pass


def conditional_probability(PAB, PB):
    """
    P(A|B) = P(A ∩ B) / P(B)
    """
    pass


def are_independent(PA, PB, PAB, tol=1e-9):
    """
    True if:
        |P(A ∩ B) - P(A)P(B)| < tol
    """
    pass


def bayes_rule(PBA, PA, PB):
    """
    P(A|B) = P(B|A)P(A) / P(B)
    """
    pass


# ============================================================
# Part 2 — Bernoulli Distribution
# ============================================================

def bernoulli_pmf(x, theta):
    """
    f(x, theta) = theta^x (1-theta)^(1-x)
    """
    pass


def bernoulli_theta_analysis(theta_values):
    """
    Returns:
        (theta, P0, P1, is_symmetric)
    """
    pass


# ============================================================
# Part 3 — Normal Distribution
# ============================================================

def normal_pdf(x, mu, sigma):
    """
    Normal PDF:
        1/(sqrt(2π)σ) * exp(-(x-μ)^2 / (2σ^2))
    """
    pass


def normal_histogram_analysis(mu_values,
                              sigma_values,
                              n_samples=10000,
                              bins=30):
    """
    For each (mu, sigma):

    Return:
        (
            mu,
            sigma,
            sample_mean,
            theoretical_mean,
            mean_error,
            sample_variance,
            theoretical_variance,
            variance_error
        )
    """
    pass


# ============================================================
# Part 4 — Uniform Distribution
# ============================================================

def uniform_mean(a, b):
    """
    (a + b) / 2
    """
    pass


def uniform_variance(a, b):
    """
    (b - a)^2 / 12
    """
    pass


def uniform_histogram_analysis(a_values,
                               b_values,
                               n_samples=10000,
                               bins=30):
    """
    For each (a, b):

    Return:
        (
            a,
            b,
            sample_mean,
            theoretical_mean,
            mean_error,
            sample_variance,
            theoretical_variance,
            variance_error
        )
    """
    pass


if __name__ == "__main__":
    print("Implement all required functions.")
