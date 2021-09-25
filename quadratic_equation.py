# 25.09.2021 - Mohammad Ali Sakib 
# ---------- Process of Program Planing ---------------
# 1. Problem Identification- Quadratic Problem Solution 
# 2. System Analysis - Formula = (-b +- sqrt(b^2 - 4ac))
# 3. Input-Output - input a,b,c and output= x value
# 4. Algorithm Development - Follow Program comment 
# 5. FlowChart Development - Follow Program comment 
# 6. Programming Language = Python 
# 7. Program  Coding - Bellow Line
# 8. Compile Code - type command - 'python3 quadratic_equation.py'
# 9. Program Testing and Debug - Working fine 
# 10. Documentation - Not included
# 11. Installation - Working Perfectly
# 12. Maintenance - Future Hope 

# ------------Algorithm and Code Below ------------
# 4.1- Program Start
import math
# 4.2 - input a,b,c
a = int(input('Enter first Number :- '))
b = int(input('Enter second Number :- '))
c = int(input('Enter third Number :- '))

# 4.3 - Define Nishcayok value 
d = math.pow(b,2)-(4*a*c)
# 4.4 - if d>0 then  define x1 and x2 value or if d==0 then x=-b/2a or else then return 'Roots are imaginery Number '
if d>0:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    print('The Ans is :- x1 ={} and x2 = {} '.format(x1,x2))
elif d==0:
    x = -b / (2*a)
    print('The Ans is :- ',x)
else:
    print('Roots are imaginery Number!')
# 4.5 - Program End