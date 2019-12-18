#!/usr/bin/env python3

"""
main entrypoint
"""

from mb import MotherBoard


def main():
    mb = MotherBoard()

    # Some fake data to render
    j = [3, 3, 3, 3, 3, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 3, 1, 3, 1, 1, 3, 3, 3, 1, 1]
    ##mb.gpu.map(0x0, j)

    print('==== INITIALIZED ====')
    print('==== cpu: ====')
    print(f'{mb.cpu}')
    print('==== mem ====')
    print(f'{mb.mem[:500]}')
    print(f'{mb.cpu.ld8(0x99)}')
    print(f'{mb.cpu.ld16(0x99)}')
    print(f'{mb.cpu.ld8(0x190)}')
    print(f'{mb.cpu.ld16(0x190)}')
    ##print(f'==== gpu ({mb.gpu.width}x{mb.gpu.height})({mb.gpu.resolution})====')
    ##print(f'{mb.gpu}')

    # Create test NOP sled just to start executing _something_
    nopsled = [0x00, 0x00, 0x00, 0x00, 0x00]


if __name__ == '__main__':
    main()
