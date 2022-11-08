def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    s=0
    
    d=list(range(1,N+1))
    for i in d:
        s+=1/i
    return s
print(main(4))