"""
graphical processing unit
"""

from memory import Memory


class GPU():

    CHARMAP = {
        0: '  ',
        1: '░░',
        2: '▒▒',
        3: '▓▓',
    }

    def __init__(self, w=128, h=128):
        """
        [
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]
        ]
        """
        self.width = w
        self.height = h
        self.viewport = []
        self.resolution = self.width * self.height
        self.ram = Memory(8192)  # 8k

        for i in range(self.resolution):
            self.ram[i] = 0x03

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        self.viewport = []
        n = 0
        for _ in range(self.height):
            tmp = ''
            for __ in range(self.width):
                tmp += GPU.CHARMAP[self.ram[n]]
                n += 1

            self.viewport.append(tmp)

        return '\n'.join(self.viewport)

    # def map(self, start, val):
    #     """ Map val<List[Byte]> to heap starting at <start>"""
    #     i = 0
    #     for b in val:
    #         self.ram[start+i] = b
    #         i += 1
