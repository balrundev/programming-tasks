def factorial(n: int) -> int:
    
    if type(n) is not int:
        raise TypeError('n must be integer')
    
    if n < 0:
        raise ValueError('n must be equal or greater than 0')
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    print(factorial(5))