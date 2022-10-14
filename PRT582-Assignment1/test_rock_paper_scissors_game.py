"""Testing all area functions of the project"""
from unittest import TestCase
from rock_paper_scissors_game import compare_two_moves


class CompareMovesTest(TestCase):
    """ class for testing function of comparison of two moves"""

    def test_compare_rock(self):
        """ testing the function with user move as rock"""
        self.assertTrue(compare_two_moves("rock", "rock") == 0)
        self.assertTrue(compare_two_moves("rock", "paper") == -1)
        self.assertTrue(compare_two_moves("rock", "scissors") == 1)

    def test_compare_paper(self):
        """ testing the function with user move as paper"""
        self.assertTrue(compare_two_moves("paper", "paper") == 0)
        self.assertTrue(compare_two_moves("paper", "scissors") == -1)
        self.assertTrue(compare_two_moves("paper", "rock") == 1)

    def test_compare_scissors(self):
        """ testing the function with user move as scissors"""
        self.assertTrue(compare_two_moves("scissors", "scissors") == 0)
        self.assertTrue(compare_two_moves("scissors", "rock") == -1)
        self.assertTrue(compare_two_moves("scissors", "paper") == 1)
