from math import gcd

def nth_ugly_number(n: int, a: int, b: int, c: int) -> int:
    ab = a*b // gcd(a, b)
    bc = b*c // gcd(b, c)
    ac = a*c // gcd(a, c)
    abc = ab * c // gcd(ab, c)
    
    def count_of_ugly(k: int) -> int:
        return k//a + k//b + k//c - k//ab - k//bc - k//ac + k//abc 
    
    left, right = n, n * abc
    index = right
    
    while left <= right:
        mid = (left + right) // 2
        if count_of_ugly(mid) >= n:
            index = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return index % (10**9 + 7)
            

if __name__ == '__main__':
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    res = nth_ugly_number(n, a, b, c)
    print(res)
