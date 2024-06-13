class SimilarityChecker:
    def get_score(self, first, second):
        if self.assert_illegal_argument(first, second):
            raise TypeError()

        return 40 + self.get_length_score(first, second)

    def get_length_score(self, first, second):
        if len(first) == len(second):
            return 60

    def assert_illegal_argument(self, first, second):
        return not isinstance(first, str) or not isinstance(second, str)
