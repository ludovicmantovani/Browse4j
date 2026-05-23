"""Test module for utils."""

from src.lib.utils import math_add


def test_addition():
    """Test addition."""
    assert math_add(1, 2) == 3
