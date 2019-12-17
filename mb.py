"""
motherboard
"""

from cpu import CPU
from memory import Memory
from gpu import GPU


class MotherBoard:
    """ mb """

    def __init__(self):
        self.cpu = CPU()
        self.mem = Memory()
        self.gpu = GPU(w=5, h=5)
        self.run = True               # power

    def repl(self):
        """ Read Eval Print Loop """
        while self.run:
            self.cpu.get_pc()
