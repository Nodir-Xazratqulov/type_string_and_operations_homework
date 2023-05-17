def main(x,y):
    """
    Given two integers x, y return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """
    a = (x+y)*2
    return '('+str(x)+'+'+str(y)+')'+'*'+'2'+'='+ str(a)
print(main(4,6))