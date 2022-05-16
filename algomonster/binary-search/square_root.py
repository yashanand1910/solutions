def square_root(n: int) -> int:
    sqrt = 0
    left, right = 0, n
    
    while left <= right:
        mid = (left + right) // 2
        if mid**2 > n:
            right = mid - 1
        else:
            sqrt = mid
            left = mid + 1
            
    return sqrt

if __name__ == '__main__':
    n = int(input())
    res = square_root(n)
    print(res)
