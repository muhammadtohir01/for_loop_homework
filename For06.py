def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    s=0
    d=list(range(A,B))
    for i in d:
        s+=i
    return s
print(main(-6,8))