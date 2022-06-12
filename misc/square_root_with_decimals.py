def sqrt(n, degree):
    x = n * (100 ** degree)
    left, right = 0, 1 + (x//2)
    ans = 0
    while left < right:
        mid = (left + right) // 2
        if mid**2 > x:
            right = mid - 1
        else:
            if mid ** 2 == x:
                return ans / (10 ** degree)
            left = mid + 1
    return (left - 1) / (10 ** degree)

if __name__ == '__main__':
    n, degree = input().split(' ')
    print(sqrt(int(n), int(degree)))
