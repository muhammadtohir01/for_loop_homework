def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    r=range(n)
    print(list(r))
    for i in list(r):
        return i
print(main(5))