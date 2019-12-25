"""
bitwise operations and helpers
"""

def mask(n):
    """
    create bitmask of length n
    """
    return sum(2**x for x in range(n))

def rotl(n, rotations=1, width=None):
    """
    Return a given number of bitwise left rotations of an integer n,
    for a given bit field width.
    If no width given find how many bits wide the int is. Eg '0b1111' is 6 chars -2 = 4.
    """
    width = len(bin(n))-2 if width is None else width
    rotations %= width
    if rotations < 1:
        return n
    n &= mask(width) ## Should it be an error to truncate here?
    return ((n << rotations) & mask(width)) | (n >> (width - rotations))
 
def rotr(n, rotations=1, width=None):
    """
    Return a given number of bitwise right rotations of an integer n,
    for a given bit field width.
    If no width given find how many bits wide the int is. Eg '0b1111' is 6 chars -2 = 4.
    """
    width = len(bin(n))-2 if width is None else width
    rotations %= width
    if rotations < 1:
        return n
    n &= mask(width)
    return (n >> rotations) | ((n << (width - rotations)) & mask(width))
