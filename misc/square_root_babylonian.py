def get_decimals(n, d):
    if d == 0:
        return str(n).split('.')[0]
    return str(n).split('.')[-1][:d]

def square_root(n, d=0):
    if n == 1:
        return f'%.{d}f'%n
    y = 1
    x = 1
    i = 0
    while i < 10 or get_decimals(y, d) != get_decimals(x, d):
        x = y
        y = 0.5 * (x + (n/x))
        i += 1
    return f'%.{d}f'%y

if __name__ == '__main__':
    n, d = list(map(int, input().split(' ')))
    print(square_root(n, d))
    
