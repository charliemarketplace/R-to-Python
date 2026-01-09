"""Tests for Module 8: Statistical Modeling"""

import pytest
import numpy as np
import pandas as pd
from scipy import stats


class TestEx01LinearRegression:
    """Test linear regression."""

    def test_ols_fit(self):
        import statsmodels.formula.api as smf

        df = pd.DataFrame({
            "y": [1, 2, 3, 4, 5],
            "x": [1, 2, 3, 4, 5]
        })
        model = smf.ols("y ~ x", data=df).fit()
        assert hasattr(model, 'params')
        assert "Intercept" in model.params.index


class TestEx02ModelResults:
    """Test accessing model results."""

    def test_model_attributes(self):
        import statsmodels.formula.api as smf

        df = pd.DataFrame({
            "y": [1, 2, 3, 4, 5],
            "x": [1, 2, 3, 4, 5]
        })
        model = smf.ols("y ~ x", data=df).fit()

        assert hasattr(model, 'params')
        assert hasattr(model, 'pvalues')
        assert hasattr(model, 'rsquared')
        assert 0 <= model.rsquared <= 1


class TestEx03InterceptTrap:
    """Test intercept trap with array API."""

    def test_add_constant(self):
        import statsmodels.api as sm

        X = np.array([[1], [2], [3]])
        X_with_const = sm.add_constant(X)
        assert X_with_const.shape[1] == 2


class TestEx06TTest:
    """Test t-test."""

    def test_ttest_ind(self):
        group1 = [1, 2, 3, 4, 5]
        group2 = [2, 3, 4, 5, 6]

        t_stat, p_value = stats.ttest_ind(group1, group2)
        assert isinstance(t_stat, float)
        assert 0 <= p_value <= 1


class TestEx07Correlation:
    """Test correlation."""

    def test_pearsonr(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]

        r, p = stats.pearsonr(x, y)
        assert abs(r - 1.0) < 0.001  # Perfect correlation


class TestEx08ChiSquared:
    """Test chi-squared test."""

    def test_chi2_contingency(self):
        observed = [[10, 20], [20, 40]]
        chi2, p, dof, expected = stats.chi2_contingency(observed)

        assert isinstance(chi2, float)
        assert 0 <= p <= 1
        assert dof == 1


class TestEx09Distributions:
    """Test distributions."""

    def test_norm_cdf(self):
        # P(Z < 1.96) should be approximately 0.975
        prob = stats.norm.cdf(1.96)
        assert abs(prob - 0.975) < 0.001

    def test_norm_ppf(self):
        # Quantile for 0.975 should be approximately 1.96
        z = stats.norm.ppf(0.975)
        assert abs(z - 1.96) < 0.01

    def test_norm_rvs(self):
        samples = stats.norm.rvs(size=100)
        assert len(samples) == 100
