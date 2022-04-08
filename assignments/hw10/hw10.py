"""
Name: Angie Bui
hw10.py
Problem: This program uses While loops to create
different classes, objects, decisions/repition, and 
boolean values. 
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import*
from face import*


def fibonacci(num):
    n1, n2 = 1, 1
    fib_seq = []
    count = 0
    while count < num and num > 1:
        fib_seq.append(n1)
        result = n1 + n2
        n1 = n2
        n2 = result
        count += 1
    return fib_seq[num - 1]


def double_investment(principal, rate):
    year = 0
    total = totals = principal
    while total < 2*totals:
        total = total + total * rate + 1
        year += 1
    return year


def syracuse(num):
    nums = [num]
    while num != 1:
        if (num % 2) == 0:
            eq = num // 2
            nums.append(eq)
            num = eq
        else:
            eq = num * 3 + 1
            nums.append(eq)
            num = eq
    return nums


def goldbach(num):
    # get primes
    primes = []
    val = 1
    while val <= num:
        count = 0
        i = 2
        while i <= val // 2:
            if val % i == 0:
                count = count + 1
                break
            i = i + 1
        if count == 0 and val != 1:
            primes.append(val)
        val = val + 1
    # goldy function
    if num % 2 != 0:
        return None

    idex_a = 0
    idex_b = 0
    prime_a = primes[idex_a]
    prime_b = primes[idex_b]

    while prime_a + prime_b != num:
        if prime_b == primes[-1]:
            idex_a = idex_a + 1
            idex_b = idex_a + 1
            prime_a = primes[idex_a]
            prime_b = primes[idex_b]
        else:
            idex_b = idex_b + 1
            prime_b = primes[idex_b]
    return [prime_a, prime_b]


def main():
    win = GraphWin("Face", 700, 700)
    center = Point(350, 350)
    size = 300
    my_face = Face(win, center, size)
    # my_face.wink()
    # my_face.shock()
    my_face.smile()
    win.getMouse()
    win.close()

main()
  
