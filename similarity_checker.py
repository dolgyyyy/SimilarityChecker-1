class SimilarityChecker:
    def get_score(self, first, second):
        if self.assert_illegal_argument(first, second):
            raise TypeError()

        return 100

    def assert_illegal_argument(self, first, second):
        return not isinstance(first, str) or not isinstance(second, str)
