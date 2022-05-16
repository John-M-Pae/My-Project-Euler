import unittest
import project_euler.euler0 as euler

class TestProblem1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.problem = euler.Problem1()
    
    def test_given_example(self):
        sum_of_multiples_of_3_or_5_below_10 = 23
        computed_sum = self.problem.solve(10)
        self.assertEqual(\
            sum_of_multiples_of_3_or_5_below_10,\
            computed_sum
            )