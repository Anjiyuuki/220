import math
my_range= range(0,10*2)
for i in my_range:
    print (i/2)


#accumulator
sum = 0
for i in range(101):
    sum = sum + i
    print(sum)

#Factorial of an input
fact= eval(input("Enter value to factorial:"))
acc= 1
for i in range(fact,0,-1):
    acc = i * acc
print(acc)

list(range(6,0,-1))

# Quadratic, Find root
a,b,c = eval(input("Enter a, b, and c:"))
root_1 = (-b + math.sqrt(b*b-4 * a *c ))/ (2*a)
root_2 = (-b - math.sqrt(b*b-4 * a *c ))/ (2*a)
print("Root 1:", root_1, "Root 2:", root_2)


