import unittest
import lab5

class TestUtils(unittest.TestCase):
    def test_most_common_word(self):
        self.assertEqual(lab5.most_common_word("apple banana apple"), ("apple", 2))
        self.assertEqual(lab5.most_common_word("orange orange apple banana apple apple"), ("apple", 3))
        self.assertEqual(lab5.most_common_word("one two three four five"), ("one", 1))

    def test_count_words(self):
        self.assertEqual(lab5.count_words("apple banana apple"), 3)
        self.assertEqual(lab5.count_words("orange orange apple banana apple apple"), 6)
        self.assertEqual(lab5.count_words("one two three four five"), 5)

if __name__ == '__main__':
    unittest.main()
