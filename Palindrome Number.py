def isPalindrome(num):
    res = 0
    answer = num
    while num > 0:
        res = res * 10 + num % 10
        num //= 10

    return res == answer