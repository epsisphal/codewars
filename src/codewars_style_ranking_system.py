# Codewars style ranking system from CodeWars

import codewars_test as test

class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, rank):
        if rank > 8 or rank < -8 or rank == 0:
            raise ValueError("Invalid rank")
        if self.rank == 8:
            return
        if self.rank == rank:
            self.progress += 3
        if self.rank * rank > 0: # if same sign
            if self.rank - rank == 1:
                self.progress += 1
            elif self.rank - rank >= 2:
                pass
            elif self.rank - rank <= -1:
                self.progress += 10 * (rank - self.rank) ** 2
        else: # not same sign
            if self.rank - rank == 2:
                self.progress += 1
            elif self.rank - rank >= 3:
                pass
            elif rank-self.rank >= 2:
                self.progress += 10 * (rank - self.rank - 1) ** 2
        while self.progress >= 100:
            self.progress -= 100
            self.rank += 1
            if self.rank == 0:
                self.rank += 1
        if self.rank >= 8:
            self.rank = 8
            self.progress = 0

user = User()
user.inc_progress(6)
print(user.rank)
print(user.progress)

# user.inc_progress(-4)
# print(user.progress)

def do_test(rank, expected_rank, expected_progress):
    if rank: user.inc_progress(rank)
    test.assert_equals(user.rank, expected_rank, "After applying rank of " + str(rank))
    test.assert_equals(user.progress, expected_progress, "After applying rank of " + str(rank))

# @test.it("Sample tests")
# def _():

#     global user
#     do_test(-8, -8, 3)

#     user = User()
#     do_test(-7, -8, 10)

#     user = User()
#     do_test(-6, -8, 40)

#     user = User()
#     do_test(-5, -8, 90)

#     user = User()
#     do_test(-4, -7, 60)

#     user = User()
#     do_test(1, -2, 40)
#     do_test(1, -2, 80)
#     do_test(1, -1, 20)
#     do_test(1, -1, 30)
#     do_test(1, -1, 40)
#     do_test(2, -1, 80)
#     do_test(2, 1, 20)
#     do_test(-1, 1, 21)
#     do_test(3, 1, 61)

