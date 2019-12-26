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
    cpu.fz = 0x1 if cpu.b == 0 else 0x0
    cpu.fn = 0x0
    cpu.fh = 0x1 if cpu.b > 256 else 0x0

def DEC_B(cpu):
    """ 0x05 1b 4c Z 1 H - """
    cpu.b -= 1
    cpu.fz = 0x1 if cpu.b == 0 else 0x0
    cpu.fn = 0x1
    cpu.fh = 0x1 if cpu.b > 256 else 0x0

def LD_B_D8(cpu, d):
    """ 0x06 2b 8c - - - - """
    cpu.b = d

def RLCA(cpu):
    """ 0x07 1b 4c 0 0 0 C """
    # Rotate C and put the 7th bit in reg A
    pass

def LD_A16_SP(cpu):
    """ 0x08 3b 20c - - - - """
    cpu.a = cpu.sp

def ADD_HL_BC(cpu):
    """ 0x09 1b 8c - 0 H C """
    cpu.set_hl(cpu.bc)
    cpu.fn = 0x0
    cpu.fh = 0x1 if cpu.hl > 256 else 0x0
    #cpu.fc = ?

def LD_A_BC(cpu):
    """ 0x0A 1b 8c - - - - """
    cpu.a = cpu.bc

def DEC_BC(cpu):
    """ 0x0b 1b 8c - - - -"""
    cpu.set_bc(cpu.get_bc()-1)
