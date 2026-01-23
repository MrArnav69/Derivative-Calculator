num = input("Enter the term: ")
x = int(input("Enter the value for x: "))

def derivative_calc(num, x):
    li = list(num.strip().split("^"))
    n = int(li[1])
    return n*x**(n-1)

print(derivative_calc(num, x))