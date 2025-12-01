"""Test suite for utils.py functions."""

import sys
from pathlib import Path

# Add the parent directory to Python path to import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from utils import is_palindrome, sum_even, count_vowels


class TestIsPalindrome:
    """Test cases for the is_palindrome function."""

    def test_empty_string_is_palindrome(self):
        """Test that empty string is considered a palindrome."""
        assert is_palindrome("") is True

    def test_single_character_is_palindrome(self):
        """Test that single character is a palindrome."""
        assert is_palindrome("a") is True
        assert is_palindrome("A") is True
        assert is_palindrome("1") is True

    def test_simple_palindromes(self):
        """Test simple palindrome strings."""
        assert is_palindrome("aba") is True
        assert is_palindrome("racecar") is True
        assert is_palindrome("madam") is True
        assert is_palindrome("level") is True

    def test_case_sensitive_palindromes(self):
        """Test that function is case-sensitive."""
        assert is_palindrome("Aa") is False
        assert is_palindrome("AbA") is False

    def test_numeric_palindromes(self):
        """Test palindromes with numbers."""
        assert is_palindrome("121") is True
        assert is_palindrome("1221") is True
        assert is_palindrome("12321") is True

    def test_non_palindromes(self):
        """Test strings that are not palindromes."""
        assert is_palindrome("hello") is False
        assert is_palindrome("python") is False
        assert is_palindrome("abc") is False
        assert is_palindrome("12345") is False

    def test_palindromes_with_spaces_and_punctuation(self):
        """Test strings with spaces and punctuation."""
        # These should not be palindromes due to spaces/punctuation
        assert is_palindrome("a man a plan a canal panama") is False
        assert is_palindrome("race a car") is False
        assert is_palindrome("A man, a plan, a canal: Panama") is False

    def test_even_length_palindromes(self):
        """Test palindromes with even number of characters."""
        assert is_palindrome("abba") is True
        assert is_palindrome("noon") is True
        assert is_palindrome("deed") is True

    @pytest.mark.parametrize("text,expected", [
        ("", True),
        ("a", True),
        ("aa", True),
        ("ab", False),
        ("aba", True),
        ("abc", False),
        ("racecar", True),
        ("hello", False),
    ])
    def test_palindrome_parametrized(self, text, expected):
        """Parametrized test cases for palindrome function."""
        assert is_palindrome(text) is expected


class TestSumEven:
    """Test cases for the sum_even function."""

    def test_empty_list(self):
        """Test that empty list returns 0."""
        assert sum_even([]) == 0

    def test_no_even_numbers(self):
        """Test list with only odd numbers."""
        assert sum_even([1, 3, 5, 7, 9]) == 0

    def test_only_even_numbers(self):
        """Test list with only even numbers."""
        assert sum_even([2, 4, 6, 8]) == 20

    def test_mixed_numbers(self):
        """Test list with both odd and even numbers."""
        assert sum_even([1, 2, 3, 4, 5, 6]) == 12  # 2 + 4 + 6

    def test_negative_numbers(self):
        """Test with negative numbers."""
        assert sum_even([-2, -1, 0, 1, 2]) == 0  # -2 + 0 + 2

    def test_zero_is_even(self):
        """Test that zero is considered even."""
        assert sum_even([0]) == 0
        assert sum_even([0, 1, 2]) == 2  # 0 + 2

    def test_large_numbers(self):
        """Test with larger numbers."""
        assert sum_even([100, 101, 102, 103, 104]) == 306  # 100 + 102 + 104

    def test_single_even_number(self):
        """Test list with single even number."""
        assert sum_even([4]) == 4

    def test_single_odd_number(self):
        """Test list with single odd number."""
        assert sum_even([5]) == 0

    @pytest.mark.parametrize("numbers,expected", [
        ([], 0),
        ([1, 3, 5], 0),
        ([2, 4, 6], 12),
        ([1, 2, 3, 4], 6),
        ([-2, -1, 0, 1, 2], 0),
        ([10, 15, 20, 25], 30),
    ])
    def test_sum_even_parametrized(self, numbers, expected):
        """Parametrized test cases for sum_even function."""
        assert sum_even(numbers) == expected


class TestCountVowels:
    """Test cases for the count_vowels function."""

    def test_empty_string(self):
        """Test that empty string returns 0."""
        assert count_vowels("") == 0

    def test_no_vowels(self):
        """Test string with no vowels."""
        assert count_vowels("bcdfg") == 0
        assert count_vowels("xyz") == 0

    def test_only_vowels_lowercase(self):
        """Test string with only lowercase vowels."""
        assert count_vowels("aeiou") == 5
        assert count_vowels("aeioua") == 6

    def test_only_vowels_uppercase(self):
        """Test string with only uppercase vowels."""
        assert count_vowels("AEIOU") == 5
        assert count_vowels("AEIOUA") == 6

    def test_mixed_case_vowels(self):
        """Test string with mixed case vowels."""
        assert count_vowels("AeIoU") == 5
        assert count_vowels("Hello") == 2  # e, o

    def test_words_with_vowels(self):
        """Test real words with vowels."""
        assert count_vowels("hello") == 2  # e, o
        assert count_vowels("python") == 1  # y is not considered a vowel, only o
        assert count_vowels("programming") == 3  # o, a, i
        assert count_vowels("beautiful") == 5  # e, a, u, i, u

    def test_single_vowels(self):
        """Test single vowel characters."""
        assert count_vowels("a") == 1
        assert count_vowels("e") == 1
        assert count_vowels("i") == 1
        assert count_vowels("o") == 1
        assert count_vowels("u") == 1

    def test_single_consonants(self):
        """Test single consonant characters."""
        assert count_vowels("b") == 0
        assert count_vowels("z") == 0

    def test_numbers_and_special_chars(self):
        """Test strings with numbers and special characters."""
        assert count_vowels("123") == 0
        assert count_vowels("!@#$%") == 0
        assert count_vowels("a1e2i3o4u5") == 5

    def test_repeated_vowels(self):
        """Test strings with repeated vowels."""
        assert count_vowels("aaa") == 3
        assert count_vowels("book") == 2  # o, o
        assert count_vowels("queue") == 4  # u, e, u, e

    @pytest.mark.parametrize("text,expected", [
        ("", 0),
        ("hello", 2),
        ("HELLO", 2), 
        ("aeiou", 5),
        ("AEIOU", 5),
        ("bcdfg", 0),
        ("python", 1),
        ("programming", 3),
        ("beautiful", 5),
        ("123!@#", 0),
    ])
    def test_count_vowels_parametrized(self, text, expected):
        """Parametrized test cases for count_vowels function."""
        assert count_vowels(text) == expected


# Edge case and integration tests
class TestEdgeCases:
    """Test edge cases and integration scenarios."""

    def test_very_long_strings(self):
        """Test functions with very long strings."""
        long_string = "a" * 1000
        assert count_vowels(long_string) == 1000
        assert is_palindrome(long_string) is True

    def test_unicode_characters(self):
        """Test functions with unicode characters."""
        # These should be treated as consonants (not vowels)
        assert count_vowels("café") == 2  # a, e (é is not in basic vowels)
        assert count_vowels("naïve") == 3  # a, i, e (ï is not in basic vowels)

    def test_whitespace_strings(self):
        """Test functions with whitespace."""
        assert count_vowels("   ") == 0
        assert count_vowels(" a e i ") == 3
        assert is_palindrome(" ") is True
        assert is_palindrome("a a") is False  # space breaks palindrome