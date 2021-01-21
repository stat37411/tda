"""
Utility functions for simplices
use ordered datatypes (e.g. list, tuple)
"""

def boundary(s):
    """
    generator to iterate over boundary of simplex s
    """
    for i in range(len(s)):
        yield s[:i] + s[i+1:]
