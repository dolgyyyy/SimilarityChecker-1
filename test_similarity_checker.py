from unittest import TestCase

from similarity_checker import SimilarityChecker


class TestSimilarityChecker(TestCase):
    def setUp(self):
        super().setUp()
        self.similarity_checker = SimilarityChecker()

    def assert_illegal_argument(self, first, second):
        try:
            self.similarity_checker.get_score(first, second)
            self.fail()
        except TypeError:
            pass

    def test_illegal_argument(self):
        self.assert_illegal_argument(None, "ABCDE")
        self.assert_illegal_argument("ABCDE", None)
        self.assert_illegal_argument("ABCDE", 12345)
        self.assert_illegal_argument(12345, "ABCDE")
        self.assert_illegal_argument("ABCDE", [])
        self.assert_illegal_argument([], "ABCDE")

    def test_get_score(self):
        self.assertEqual(self.similarity_checker.get_score("ABCDE", "ABCDE"), 100)
