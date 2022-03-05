import math
def convert():
    celsius = eval(input("Enter temp in celsius:"))
    fahrenheit = celsius * 9/5 + 32

    print(fahrenheit)
    if fahrenheit > 90:
        print("Wow that's hot!")
    if fahrenheit < 30:
        print("Brrrr, that's cold")

#convert()


def root(a,b,c):
# Mutually exclusive, has to be one or the other option that is True
    disc = b * b - 4 * a * c
    if disc >= 0:
        sqrt_dis = math.sqrt(disc)
        denom = 2*a
        root_1 = (-b + sqrt_dis)/denom
        root_2 = (-b - sqrt_dis)/denom
        return (root_1, root_2)
    else:
        return 'no real root', 'no real root'

if __name__ == '__main__':
    r1, r2 = root(1, 1, 1)
    print('root 1: {} | root 2: {}'.format(r1, r2))


def max(a,b, c):
    if a >= b and a>= c:
        return a
    if b>= a and b>= c:
        return b
    if c>= a and c>= b:
        return c


def max_two(a, b, c):
    if a>= b:
        if a >= c:
            return a
        else:
            return c
    if b>= c:
        return b
    return c

def max_three(a,b,c):
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    return max_value

def max_four(values):

    max_values =0
    for value in values:
        if value > max_value:
            max_value = value
    return max_value

max_four([2])