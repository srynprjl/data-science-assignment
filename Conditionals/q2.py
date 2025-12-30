## Print a multiplication table for a number, but highlight the multiples of 5

a = int(input("Enter a number: "))

for i in range(1, 11):
    p = a * i;
    if(p % 5 == 0):
        print(f"{a} * {i} = {p}, which is the multiple of 5")
    else:
        print(f"{a} * {i} = {p}")
