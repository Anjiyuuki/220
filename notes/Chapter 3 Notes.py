my_range= range(0,10*2)
for i in my_range:
    print (i/2)


#accumulator
sum = 0
for i in range(101):
    sum = sum + i
    print(sum)


fact= eval(input("Enter value to factorial:"))
acc= 1
for i in range(fact,0,-1):
    acc = i * acc
print(acc)

list(range(6,0,-1))
