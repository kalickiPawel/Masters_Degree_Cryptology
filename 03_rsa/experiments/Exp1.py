from experiments import Experiment
from random import randint
import logging

logger = logging.getLogger(__name__)


class Exp1(Experiment):
    """ 
    Experiment 1 - No - message attack
    """

    def __init__(self, size):
        super().__init__(size)
        self.s_exp1 = randint(10 ** (self.size - 1), (10 ** self.size) - 1)
        self.m_exp1 = pow(self.s_exp1, self.e, self.n)
        logger.info('>---Start the Experiment 1--<\n')

    def no_message_attack(self):
        return self.s_exp1, self.m_exp1

    def validation(self, **kwargs):
        return super().validation(self.s_exp1, self.m_exp1)
