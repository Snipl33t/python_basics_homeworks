"""
Program outputs the values which are multiples of 20 or 21 as a list
One-line program
"""

# not (itm % 20 and itm % 21) == not itm % 20 or not itm % 21
print([itm for itm in range(20, 241) if not (itm % 20 and itm % 21)])
