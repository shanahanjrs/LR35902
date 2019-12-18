"""
cpu class
"""

from time import sleep

from memory import Memory


class CPU:
    def __init__(self, mem=Memory()):
        """
        little endian cpu
        +-------------+-------------- +--------------+
        | Instruction | Least Signif- | Most Signif-
        | Identifier  | icant Byte    | icant Byte   |
        +-------------+-------------- +--------------+
        registers:
          8bit  Hi   Low Name/Function
          A              Accumulator
          B
          C
          D
          E
          F               Flags
          H
          L
          AF    A    -    Accumulator & Flags
          BC    B    C    BC
          DE    D    E    DE
          HL    H    L    HL
          SP    -    -    Stack Pointer
          PC    -    -    Program Counter/Pointer

        Most registers can be accessed either as one 16bit register, or as two separate 8bit registers

        The Flag Register (lower 8bit of AF register)
          Bit  Name  Set Clr  Expl.
          7    zf    Z   NZ   Zero Flag
          6    n     -   -    Add/Sub-Flag (BCD)
          5    h     -   -    Half Carry Flag (BCD)
          4    cy    C   NC   Carry Flag
          3-0  -     -   -    Not used (always zero)
        """
        self.SLEEPDUR = 0.01667  # tick rate 60Hz
        self.REDRAWRATE = 9      # Num of cycles before we redraw the screen
        self.mem = mem           # heap
        self.a = 0x0             # registers
        self.b = 0x0
        self.c = 0x0
        self.d = 0x0
        self.e = 0x0
        self.fz = 0x0            # zero flag
        self.fn = 0x0            # subtraction flag
        self.fh = 0x0            # half carry flag
        self.fc = 0x0            # carry flag
        self.h = 0x0
        self.l = 0x0
        self.sp = 0x0            # stack pointer
        self.pc = 0x0100         # program counter - start at 0x0100
        self.cycles = 0          # Cycles counter, then frame draw, then reset to 0. (9 Cycles before a redraw)
        self.ins = None

    def __str__(self):
        return str({
            'a': hex(self.a),
            'b': hex(self.b),
            'c': hex(self.c),
            'd': hex(self.d),
            'e': hex(self.e),
            'fz': hex(self.fz),
            'fn': hex(self.fn),
            'fh': hex(self.fh),
            'fc': hex(self.fc),
            'h': hex(self.h),
            'l': hex(self.l),
            'sp': hex(self.sp),
            'pc': hex(self.pc)
            })

    def get_pc(self):
        """ get instruction at Program Counter """
        pc = self.mem[self.pc]
        self.pc += 0x01
        if pc == '0xCB':  # prefixed instruction, read next byte as well
            pc += self.mem[self.pc]
            self.pc += 0x01

        return pc

    def set_bc(self, val):
        """ sets the BC register """
        self.b = val >> 8
        self.c = val & 0x00FF

    def set_de(self, val):
        """ DE """
        self.d = val >> 8
        self.e = val & 0x00FF

    def tick(self):
        """ One cycle. Check if we need to render. """
        sleep(self.SLEEPDUR)
        self.cycles += 1

        if self.cycles >= self.REDRAWRATE:
            # draw here
            self.cycles = 0

    def ld8(self, addr):
        """ load 8 bits from a memory address """
        return self.mem[addr]

    def ld16(self, addr):
        """ load 16 bits from a memory address """
        return (self.mem[addr] >> 8)|(self.mem[addr+1])  # TODO: ?
