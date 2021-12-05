# quadratic equation solver - 4.12.2021
def quadratic_equation():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    #  find out the discriminant
    d = (b**2) - 4*a*c 
    if d < 0:
        print('Roots are imaginary')
    elif d == 0:
        x = (-b / (2*a))
        print('Root is', x)
    else:
        x1 = (-b + d ** 0.5) / (2*a)
        x2 = (-b - d ** 0.5) / (2*a)
        print('Roots are', x1, 'and', x2)
quadratic_equation()
