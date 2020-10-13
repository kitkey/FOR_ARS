class Worker:
    def __init__(self, n):
        self.cost = n
    def wage_non(self, m):
        return self.cost * m * 8
    def wage(self, m):
        return self.wage_non(m) * 0.13
