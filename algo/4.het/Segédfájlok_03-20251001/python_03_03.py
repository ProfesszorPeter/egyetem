def fibonacci_rek(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rek(n-1) + fibonacci_rek(n-2)

def fibonacci_dinamikus(n):
    if n <= 1:
        return [0]
    else:
        fib_numbers = [1, 1]
        for i in range(2, n):
            fib_numbers.append(fib_numbers[i-1] + fib_numbers[i-2])
        return fib_numbers

def fibonacci_dinamikus2(n, memo={}):
    if n in memo: # Ha az érték már megvan a memo-ban, akkor azt visszaadjuk
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_dinamikus2(n-1, memo) + fibonacci_dinamikus2(n-2, memo)
    print(memo,end=", ") # memo felépítése
    return memo[n]


n = 10
print(f"dinamikus2: {fibonacci_dinamikus2(n)}")
print(f"dinamikus: {fibonacci_dinamikus(n)}")
# ciklus segítségével írjuk ki a rekurziv függvénnyel a számsor elemeit

for i in range(1,n+1):
    print(fibonacci_rek(i), end=" " )

