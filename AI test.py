import unittest
import random

class TestAI(unittest.TestCase):

    def test_ai_turn(self):
        """
        Test the AI turn logic.
        """
        for _ in range(100):
            score = ai_turn()
            self.assertTrue(score >= 0)

if __name__ == '__main__':
    unittest.main()
