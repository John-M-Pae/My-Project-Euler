"""
Contains solutions to the first 10 Euler problems.

Problems completed:

Problems in progress:
    1
Problems not yet started:
    2-10
"""
from utils.problem_template import EulerProblem
import utils.logger as logger

log = logger.project_logger()

class Problem1(EulerProblem):
    def __init__(self) -> None:
        super().__init__(1)
    
    def info(self) -> str:
        return "Find the sum of all the multiples of 3 or 5 below 1000."
    
    def solve(self, num=1000) -> int:
        return num