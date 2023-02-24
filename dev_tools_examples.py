# %% [markdown]

# # Today's Topics:
# 1. Testing
# 2. Formatting
# 3. Writing Readable Code
# 4. Further Recommended Resources
# 
# Note: You can run this file in a pre-installed environment here:
# [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/FabianBarrett/dev-tools-shoshlab/main)

# %% [markdown]

# ## Testing

# * When writing lots of code, we want to be able to verify the properties of the code we've written.
# * One way of doing this is to write tests, in which we (as coders) come up with examples, run our code on those examples, and verify that the behavior of our code is as expected.
#
# There are lots of different kinds of tests, some of the most common of which are:
# * Unit tests: test isolated properties ("units") of the code.
# * Integration tests: test how one bit of code interacts ("integrates") with another bit of code.
# * Regression tests: test how the current version of the code (or data) compares to a previous version (whether the code has "regressed").
# * ...
#
# Here, we'll run through some of the functionality of a well-known testing package in Python, `pytest`.
# The principles here translate to many other frameworks.
# We will focus on unit tests for now.

# %%

import pytest

# %%

# Helper function to validate inputs
def validate_type(_input):
    return type(_input) in (int, float)


# %%

# Define some variants of a function that performs addition
def x_plus_y(x, y):
    return x + y


# Do the same as above, but validate the inputs and return an error if the inputs cannot be added
def x_plus_y_errorhandling(x, y):
    if validate_type(x) and validate_type(y):
        return x + y
    else:
        raise TypeError("Input types are not appropriate for addition.")


# %%

# Note: In `pytest`, tests take the form of a function whose names match `test_*`

# Run the test for a single example
def test_x_plus_y_basic(x=2, y=2):
    assert x_plus_y(x, y) == 4

# Run the test such that we expect it to fail
def test_x_plus_y_expect_to_fail(x=2, y=2):
    assert x_plus_y(x, y) == 5


# Run the test for multiple (pairwise-specified) examples
@pytest.mark.parametrize("x, y, expected_result", [(2, 2, 4), (2, 3, 5)])
def test_x_plus_y_less_basic(x, y, expected_result):
    assert x_plus_y(x, y) == expected_result


# Run the test for multiple examples, specifying only each input separately
@pytest.mark.parametrize("x", [2, 3, 4])
@pytest.mark.parametrize("y", [3, 4, 5])
def test_x_plus_y_cartesian_product(x, y):
    # This is a trivial test, but the point is to demonstrate that pytest expands the set of test examples automagically
    assert x_plus_y(x, y) == (x + y)


# Validate that errors are raised
@pytest.mark.parametrize("x, y", [(2, "2")])
def test_x_plus_y_even_less_basic(x, y):
    with pytest.raises(TypeError):
        x_plus_y_errorhandling(x, y)


# %% [markdown]

# We can execute specific tests by running e.g.:
# ```
# pytest dev_tools_examples.py::test_x_plus_y_basic
# ```
# We can execute all tests in a file by running:
# ```
# pytest dev_tools_examples.py
# ```
# We can get the verbose version by running:
# ```
# pytest dev_tools_examples.py -vv
# ```

# %%

# Exercise: Given a normal distribution with a given mean, check that the mean of samples from it converges to the mean for different numbers of samples

# %% [markdown]

# ## Formatting

# When working with multiple co-authors or on large projects, it can be helpful to maintain consistency in style via a formatter.
# A formatter modifies code to conform to certain style rules, e.g. only using tabs vs. spaces, breaking lines over 80 characters, etc.
# Formatters thus make code more homogeneous and readable, making it:
# * Easier for newcomers to pick up patterns across different files.
# * Easier to spot mistakes.
# * ...
#
# Most languages have their own formatter, e.g. Julia has [`JuliaFormatter.jl`](https://github.com/domluna/JuliaFormatter.jl), R has [`styler`](https://styler.r-lib.org/), and Python has `black`, `isort`
# (and other tools such as `mypy` that we won't talk about today).
# Note that there are VS Code extensions (as well as command line options) for most of these.

# %%

# E.g. if I'm using a lot of different libraries, I might want them to be organized in a certain way (to minimize searching time)
# This is where `isort` can help

# Compare before and after (notice the grouping of e.g. the standard libraries)
import numpy as np
from collections import Counter
import functools
from math import sqrt

# %% [markdown]

# You can experiment with the utility of a formatter like `black` in [this playground](https://black.vercel.app/?version=stable&state=_Td6WFoAAATm1rRGAgAhARYAAAB0L-Wj4ARsAnNdAD2IimZxl1N_WlkPinBFoXIfdFTaTVkGVeHShArYj9yPlDvwBA7LhGo8BvRQqDilPtgsfdKl-ha7EFp0Ma6lY_06IceKiVsJ3BpoICJM9wU1VJLD7l3qd5xTmo78LqThf9uibGWcWCD16LBOn0JK8rhhx_Gf2ClySDJtvm7zQJ1Z-Ipmv9D7I_zhjztfi2UTVsJp7917XToHBm2EoNZqyE8homtGskFIiif5EZthHQvvOj8S2gJx8_t_UpWp1ScpIsD_Xq83LX-B956I_EBIeNoGwZZPFC5zAIoMeiaC1jU-sdOHVucLJM_x-jkzMvK8Utdfvp9MMvKyTfb_BZoe0-FAc2ZVlXEpwYgJVAGdCXv3lQT4bpTXyBwDrDVrUeJDivSSwOvT8tlnuMrXoD1Sk2NZB5SHyNmZsfyAEqLALbUnhkX8hbt5U2yNQRDf1LQhuUIOii6k6H9wnDNRnBiQHUfzKfW1CLiThnuVFjlCxQhJ60u67n3EK38XxHkQdOocJXpBNO51E4-f9z2hj0EDTu_ScuqOiC9cI8qJ4grSZIOnnQLv9WPvmCzx5zib3JacesIxMVvZNQiljq_gL7udm1yeXQjENOrBWbfBEkv1P4izWeAysoJgZUhtZFwKFdoCGt2TXe3xQ-wVZFS5KoMPhGFDZGPKzpK15caQOnWobOHLKaL8eFA-qI44qZrMQ7sSLn04bYeenNR2Vxz7hvK0lJhkgKrpVfUnZrtF-e-ubeeUCThWus4jZbKlFBe2Kroz90Elij_UZBMFCcFo0CfIx5mGlrINrTJLhERszRMMDd39XsBDzpZIYV4TcG7HoMS_IF8aMAAAxI-5uTWXbUQAAY8F7QgAAP01Vc6xxGf7AgAAAAAEWVo=).

# %% [markdown]

# ## Writing Readable Code

# See `.pdf`. 

# %% [markdown]

# ## Recommended Resources
# 
# If you want to keep looking into these tools and read on, I've found these to be useful starting points in the past:
# 1. [The Missing Semester Of Your CS Education](https://missing.csail.mit.edu/)
# 2. [The Art Of Readable Code](https://mcusoft.files.wordpress.com/2015/04/the-art-of-readable-code.pdf)
# 3. Reproducible Code Through Environments: e.g. [`renv`](https://rstudio.github.io/renv/articles/renv.html) or [`conda`](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

# %%

# %% [markdown]

# **Possible solution to the exercise above:**
# ```
# import numpy as np
# 
# @pytest.mark.parametrize(
#     "n_samples, atol", [(1000, 1e-1), (10000, 1e-2), (100000, 1e-3)]
# )
# def test_convergence(n_samples, atol):
#     # Mean 0, standard deviation of 1
#     samples = np.random.normal(size=n_samples)
#     # Here, we don't care about equality; we just care about the answer being close enough
#     assert np.isclose(np.mean(samples), 0, atol=atol)
# ```

# %%
