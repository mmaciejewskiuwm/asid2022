# def numbers(n: int):
#     if n < 0:
#         return
#     print(n)
#     numbers(n - 1)
#
#
# numbers(10)


# def power(number: int, n: int) -> int:
#     if n==0:
#         return 1
#     if n > 0:
#         return number * power(number, n - 1)
#
#
#
#
# print(power(2, 3))
# def fib(n: int) -> int:
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if n > 1:
#         return fib(n - 1) + fib(n-2)
# print(fib(9))
# def factorial(n: int) -> int:
#     if n == 0 or n == 1:
#         return 1
#     if n > 1:
#         return n * (factorial(n - 1))
#
#
#  print(factorial(4))
def helper(n: int):
    if n>0:
        return helper(n - 1)


def remove_duplicates(txt: str):
    n = len(txt)
    if n == 0:
        return txt
    return txt[helper(n*-1)]


print(remove_duplicates('amonguuus'))
