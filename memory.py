"""
memory class
"""


class Memory:
    """
    General Memory Map
    0000-3FFF   16KB ROM Bank 00     (in cartridge, fixed at bank 00)
    4000-7FFF   16KB ROM Bank 01..NN (in cartridge, switchable bank number)
    8000-9FFF   8KB Video RAM (VRAM) (switchable bank 0-1 in CGB Mode)
    A000-BFFF   8KB External RAM     (in cartridge, switchable bank, if any)
    C000-CFFF   4KB Work RAM Bank 0 (WRAM)
    D000-DFFF   4KB Work RAM Bank 1 (WRAM)  (switchable bank 1-7 in CGB Mode)
    E000-FDFF   Same as C000-DDFF (ECHO)    (typically not used)
    FE00-FE9F   Sprite Attribute Table (OAM)
    FEA0-FEFF   Not Usable
    FF00-FF7F   I/O Ports
    FF80-FFFE   High RAM (HRAM)
    FFFF        Interrupt Enable Register
    """
    VALID_MEM_TYPES = ['int', 'byte']

    def __init__(self, size=65535):
        self.__heap = bytearray([0x00]*size)

        # 0x0000 through 0x00FF are for bootstrapping (fill with nothing for now
        for i in range(0x00FF):
            self.__heap[i] = 0x01

    def __getitem__(self, key):
        return self.__heap[key]

    def __setitem__(self, key, val):
        # TODO check bounds so we dont write to "unusable" RAM Eg FEA0-FEFF
        # TODO check and make sure we implement Echo RAM for (C000-DDFF & E000-FDFF)
        self.__heap[key] = val

    def __str__(self):
        return str(self.__heap)

    def __repr__(self):
        return self.__str__()

    def map(self, start, val):
        """ Map val<List[Byte]> to heap starting at <start>
        Eg
        RAM: [\x00\x00\x00\x00]
        map(0x0, [0x01, 0xFF]
        RAM: [\x01\xFF\x00\x00]
        """
        i = 0
        for b in val:
            self.__heap[start+i] = hex(b)
            i += 1
