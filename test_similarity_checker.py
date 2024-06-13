from unittest import TestCase

from similarity_checker import SimilarityChecker


class TestSimilarityChecker(TestCase):
    def setUp(self):
        super().setUp()
        self.similarity_checker = SimilarityChecker()

    def test_get_score(self):
        self.assertEqual(self.similarity_checker.get_score("ABCDE", "ABCDE"), 100)
