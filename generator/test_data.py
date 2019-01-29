class TestData:

    def __repr__(self):
        res = ""
        if hasattr(self, "expression"):
            res += self.expression
        if hasattr(self, "result"):
            res += self.result
        return res
