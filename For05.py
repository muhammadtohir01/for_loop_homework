def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    d=list(range(A,B+1))
    return d[::-1]
print(main(5,9))