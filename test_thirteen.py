#!/usr/bin/env python3
"""
Tests for the thirteen.py module.
"""

import unittest
from thirteen import to_roman, to_english, is_prime

class TestThirteen(unittest.TestCase):
    """Test cases for thirteen functions."""

    def test_to_roman(self):
        """Test Roman numeral conversion."""
        self.assertEqual(to_roman(13), "XIII")

    def test_to_english(self):
        """Test English word conversion."""
        self.assertEqual(to_english(13), "thirteen")

    def test_is_prime(self):
        """Test prime number checking."""
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(14))
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(1))

if __name__ == "__main__":
    unittest.main()