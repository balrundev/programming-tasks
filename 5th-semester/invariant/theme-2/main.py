from itertools import islice, takewhile

def fib(n):
    res_lst = [0, 1]
    if n == 0:
        return res_lst[:1]
    elif n == 1:
        return res_lst
    elif n > 1:
        while True:
            cur_el = sum(res_lst[len(res_lst) - 2::])
            if cur_el <= n:
                res_lst.append(cur_el)
            else:
                break
        return res_lst
    else:
        return list()


class FibonacchiLst:
    def __init__(self, max_value):
        self.max_value = max_value
        self.lst = [0, 1]
    
    def __getitem__(self, idx):
        if self.max_value < 0:
            raise IndexError(idx)
        
        if idx > 0:
            if self.max_value == 0:
                raise IndexError(idx)
                        
            if idx == 1:
                return self.lst[1]
            
            if idx == 2 and self.max_value == 1:
                raise IndexError(idx)
            
            cur_el = self.lst[0] + self.lst[1]
            del self.lst[0]
            self.lst.append(cur_el)
            
            if cur_el > self.max_value:
                raise IndexError(idx)
            
            return self.lst[1]
        
        else:
            return self.lst[0]
        
        
def fib_se():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fib_iter(numbers):
    return takewhile(lambda x: x <= max(numbers), fib_se())


def fib_cl():
    lst = [0, 1]
    yield lst[0]
    yield lst[1]
    while True:
        cur_el = lst[0] + lst[1]
        del lst[0]
        lst.append(cur_el)
        yield lst[1]


def main():
    print('Function fib():')
    print(fib(10))
    print()
    
    print('FibonacchiLst():')
    print(list(FibonacchiLst(10)))
    print()
    
    print('FibonacchiLst():')
    fib_lst = FibonacchiLst(10)
    for el in fib_lst:
        print(el, end=' ')
        
    print('\n\nFunction fib_se():')
    print(list(islice(fib_se(), 7)))
    print()
    
    print('Function fib_iter() with range(25):')
    fib_lst = fib_iter(range(25))
    for el in fib_lst:
        print(el, end=' ')
        
    print('\n\nFunction fib_cl():')
    g = fib_cl()
    el = next(g)
    print(el, end=' ')
    while True:
        el = next(g)
        print(el, end=' ')
        if el > 10:
            break


if __name__ == '__main__':
    main()