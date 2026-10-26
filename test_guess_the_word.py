# Hernan Villegas
# CIS256 Fall 2026
# Programming Assignment 4

from guess_the_word import words, choose_word, check_guess


# Test that the chosen word is from the word list
def test_choose_word():
    word = choose_word()
    assert word in words


# Test a correct letter guess
def test_correct_guess():
    assert check_guess("apple", "a") is True


# Test an incorrect letter guess
def test_incorrect_guess():
    assert check_guess("apple", "z") is False


# Test a letter that appears multiple times
def test_repeated_letter():
    assert check_guess("banana", "a") is True
