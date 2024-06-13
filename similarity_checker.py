class SimilarityChecker:
    def get_score(self, first, second):
        if not isinstance(first, str) or not isinstance(second, str):
            raise TypeError()

        return 100
