"""
bitwise operations and helpers
"""


def get_bit(k, v):
    """
    gets the k bit from Int v
    0b0011 <- 1st bit
      ^- 4th bit
    Ex:
    get_bit(1, 0b0011) -> 1
    get_bit(2, 0b0011) -> 1
    get_bit(3, 0b0011) -> 0
    get_bit(4, 0b0011) -> 0
    """
    return int((v & (1 << k-1)) != 0)


def mask(n):
    """
    create bitmask of length n
    """
    return sum(2**x for x in range(n))


def rotl(n, rotations=1, width=None):
    """
    Return a given number of bitwise left rotations of an integer n,
    for a given bit field width.
    """
    width = n.bit_length() if width is None else width
    rotations %= width
    if rotations < 1:
        return n
    n &= mask(width)
    return ((n << rotations) & mask(width)) | (n >> (width - rotations))

 
def rotr(n, rotations=1, width=None):
    """
    Return a given number of bitwise right rotations of an integer n,
    for a given bit field width.
    """
    width = n.bit_length() if width is None else width
    rotations %= width
    if rotations < 1:
        return n
    n &= mask(width)
    return (n >> rotations) | ((n << (width - rotations)) & mask(width))
