from worker import Worker
class Manager(Worker):
    def __init__(self, n, bonus):
        super().__init__(n)
        self.bonus = bonus
    def wage_non(self, m):
        worker_money = Worker.wage_non(self, m)
        return worker_money * (1 + self.bonus/100)
    def wage(self, m):
        return Worker.wage_non(self, m) * 0.13
