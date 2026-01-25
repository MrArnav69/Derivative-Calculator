f_x = input("Enter the function: ")
x = int(input("Enter the value for x: "))

def derivative_calc(f_x, x):
    li = list(f_x.strip().split("/"))
    numerator = li[0]
    denominator = li[1]
    
    num_li = list(numerator.strip().split("^"))
    denom_li = list(denominator.strip().split("^"))
    
    n_num = int(num_li[1])
    n_denom = int(denom_li[1])
    
    derivative_numerator = n_num * x**(n_num - 1)
    derivative_denominator = -n_denom * x**(-n_denom - 1)
    
    return (derivative_numerator * x**(-n_denom) - numerator * derivative_denominator) / (x**(-n_denom))**2

print("The derivative of the function is:", derivative_calc(f_x, x))