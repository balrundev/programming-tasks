'''
2.3 Разработка функции-декоратора, вычисляющей время выполнения декорируемой функции.
'''

def function_timer(function):

    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        value = function(*args, **kwargs)
        finish = time.time()
        return value, finish - start

    return wrapper


@function_timer
def test_function(a, b):
    import time
    time.sleep(0.5)
    return a + b
    
    
print(test_function(10, 15))