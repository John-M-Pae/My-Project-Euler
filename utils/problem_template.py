"""
COntains abstract class structure for Euler problems.
"""
from abc import ABC, abstractmethod

class EulerProblem(ABC):
    problem_id : int

    def __init__(self, id:int) -> None:
        self.problem_id = id
    
    def link(self) -> str:
        """
        Returns a link to the problem's webpage        
        """
        return f"https://projecteuler.net/problem={self.problem_id}"

    @abstractmethod
    def info(self) -> str:
        """
        Returns a breaf description of the problem.
        """
        pass
    
    @abstractmethod
    def solve(self):
        """
        Calculates and returns the solution to the problem.
        """
        pass
