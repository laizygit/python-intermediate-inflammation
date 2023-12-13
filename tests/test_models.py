"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

def cheering(func):
    def wrapper(*args, **kwargs):
        out = func(*args, **kwargs)
        print(f'YEAH!!! {func.__name__} PASSED!!!')
        return out
    return wrapper


@cheering
def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


@cheering
def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from inflammation.models import daily_mean

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0, 0], [0, 0, 0], [0, 0, 0] ], [0, 0, 0]),
        ([ [4, 2, 5], [1, 6, 2], [4, 1, 9] ], [4, 6, 9]),
        ([ [4, -2, 5], [1, -6, 2], [-4, -1, 9] ], [4, -1, 9]),
    ])
def test_daily_max(test, expected):
    """Test max function works for zeroes, positive integers, mix of positive/negative integers."""
    from inflammation.models import daily_max
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))


@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0, 0], [0, 0, 0], [0, 0, 0] ], [0, 0, 0]),
        ([ [4, 2, 5], [1, 6, 2], [4, 1, 9] ], [1, 1, 2]),
        ([ [4, -2, 5], [1, -6, 2], [-4, -1, 9] ], [-4, -6, 2]),
    ])
def test_daily_min(test, expected):
    """Test min function works for zeroes, positive integers, mix of positive/negative integers."""
    from inflammation.models import daily_min
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))



@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0,0,0], [0,0,0], [0,0,0] ], [0,0,0,]),
        ([ [1,2,3], [3,2,1], [4,5,6] ], [1.24721913, 1.41421356, 2.05480467]),
    ])

def test_daily_std(test, expected):
    """Test std function"""
    from inflammation.models import daily_std
    npt.assert_allclose(daily_std(np.array(test)), np.array(expected))
...

@cheering
def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])


@cheering
def test_daily_std():
    from inflammation.models import daily_std
    npt.assert_almost_equal(
        daily_std(np.array([[0, 0, 0], [.5, .5, .5], [1, 1, 1]])),
        np.array([0.4082482904, 0.4082482904, 0.4082482904])
    )
