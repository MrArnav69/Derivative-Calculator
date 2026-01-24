num = input("Enter the term: ")
x = int(input("Enter the value for x: "))

def derivative_calc(num, x):
    li = list(num.strip().split("^"))
    n = int(li[1])
    return n*x**(n-1)

def derivative_formula(num):
    li = list(num.strip().split("^"))
    n = int(li[1])
    return f"{n}x^{n-1}"

print("The derivative of the term is:", derivative_calc(num, x))
print("The derivative formula is:", derivative_formula(num))