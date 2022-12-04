# Student agent: Add your own agent here
from agents.agent import Agent
from store import register_agent
import sys


@register_agent("student_agent")
class StudentAgent(Agent):
    """
    A dummy class for your implementation. Feel free to use this class to
    add any helper functionalities needed for your agent.
    """

    def __init__(self):
        super(StudentAgent, self).__init__()
        self.name = "StudentAgent"
        self.dir_map = {
            "u": 0,
            "r": 1,
            "d": 2,
            "l": 3,
        }

    def step(self, chess_board, my_pos, adv_pos, max_step):
        """
        Implement the step function of your agent here.
        You can use the following variables to access the chess board:
        - chess_board: a numpy array of shape (x_max, y_max, 4)
        - my_pos: a tuple of (x, y)
        - adv_pos: a tuple of (x, y)
        - max_step: an integer

        You should return a tuple of ((x, y), dir),
        where (x, y) is the next position of your agent and dir is the direction of the wall
        you want to put on.

        Please check the sample implementation in agents/random_agent.py or agents/human_agent.py for more details.
        """
        # dummy return
        """
        plan:
        tree implementation:
        dictionary : we would have to map each move to a key - we can use strings?
            have multiple dictionaries, one for the values, one for the list of children
        
        could also make a nested class to make code more readable

        simulating a node (default policy) - just make random moves, - fast simulations
        
        tree policy - choose an epsilon value (we can use 0.15 for now and change later)
            1-epsilon of the time, we choose node with best winrate(if n/a then choose random node)
            epsilon of the time, we choose random node

        max height of the tree? 10 for now

        how many simulations? 100-200 simulations total?

        how many total times do we expand nodes? 50?
        
        """
        return my_pos, self.dir_map["u"]
