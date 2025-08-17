# System Modules
import sys
import os

# Installed Modules
# None

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402

import pytest


def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    radius = 1
    result = area_of_circle(radius)
    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    radius = 0
    result = area_of_circle(radius)
    assert result == 0


def test_area_of_circle_negative_radius():
    """Test with a negative radius to raise ValueError."""
    radius = -1
    with pytest.raises(ValueError):
        area_of_circle(radius)


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    n = 0
    result = get_nth_fibonacci(n)
    assert result == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    n = 1
    result = get_nth_fibonacci(n)
    assert result == 1


def test_get_nth_fibonacci_ten():
    """Test with n=10."""
    n = 10
    result = get_nth_fibonacci(n)
    assert result == 55


def test_get_nth_fibonacci_negative():
    """Test with a negative number to raise ValueError."""
    n = -1
    with pytest.raises(ValueError):
        get_nth_fibonacci(n)
