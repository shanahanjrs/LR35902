"""
opcodes

https://www.pastraiser.com/cpu/gameboy/gameboy_opcodes.html

Instr mnemonic -> |  INS reg  |
Length Bytes   -> |  2     8  | <- duration (cycles)
Flags          -> |  Z N H C  |
> Inline version of this: | INS reg 2b 8c Z N H C |

Flag register (F) bits (3,2,1,0 always zero):
7 	6 	5 	4 	3 	2 	1 	0
Z 	N 	H 	C 	0 	0 	0 	0

Z zero
N subtraction
H half carry
C carry

d8  means immediate 8 bit data
d16 means immediate 16 bit data
a8  means 8 bit unsigned data, which are added to $FF00 in certain instructions (replacement for missing IN and OUT instructions)
a16 means 16 bit address
r8  means 8 bit signed data, which are added to program counter

LD A,(C) has alternative mnemonic LD A,($FF00+C)
LD C,(A) has alternative mnemonic LD ($FF00+C),A
LDH A,(a8) has alternative mnemonic LD A,($FF00+a8)
LDH (a8),A has alternative mnemonic LD ($FF00+a8),A
LD A,(HL+) has alternative mnemonic LD A,(HLI) or LDI A,(HL)
LD (HL+),A has alternative mnemonic LD (HLI),A or LDI (HL),A
LD A,(HL-) has alternative mnemonic LD A,(HLD) or LDD A,(HL)
LD (HL-),A has alternative mnemonic LD (HLD),A or LDD (HL),A
LD HL,SP+r8 has alternative mnemonic LDHL SP,r8
"""

def NOP():
    """ 0x00 1b 4c - - - -"""
    pass

def STOP():
    """ 0x10 2b 4c - - - - """
    pass

def LD_BC_D16(cpu, d):
    """ 0x01 3b 12c - - - - Load 16bit data into BC"""
    cpu.set_bc(d)

def LD_BC_A(cpu):
    """ 0x02 1b 8c - - - - Load A into BC"""
    cpu.set_bc(cpu.a)

def INC_BC(cpu):
    """ 0x03 1b 8c - - - - """
    cpu.bc += 1

def INC_B(cpu):
    """ 0x04 1b 4c Z 0 H - """
    cpu.b += 1
    # set flag Z0H-