# 25.09.2021 - Mohammad ali Sakib
# -----------------Process of Program planing -------------
# 1. Problem Identify - (( Find the value of factorial number given by user ))
# 2. System Analysis - n! = n * (n-1) * (n-2) * (n-3).....*1
# 3. Input/Output - input n 
# 4. Algorithm Development - See Program comment
# 5. FlowChart Development - Program process 
# 6. Programming Language - Python 
# 7. Program Code - Bellow writing Program
# 8. Compile code - 'python3 factorial.py'
# 9. Program Testing and Debuging - Working fine 
# 10. Documentation - Not yet Possible 
# 11. Installation - Working Perfectly
# 12. Maintenance - Future Hope

# Algorithm and coding start Here
# 1. Programme start 
# 2. input n value 
n = int(input('Enter Number: '))
fact =1
# 3. if n <0 then print 'Negative value are not allowed
if n<0:
    print('Negative numbers are not allowed. ')
# 4. if n=0 or n=1 then fact value 1 
else: 
    if (n==1 or n==0): 
        print('{}! = {}'.format(n,fact))
    else:
        # 4. when n value are bigger then 1 then create a loop and excute fact = fact +1
        for i in range(2,n+1):
            fact *=i
        # then print value
        print('{}! = {}'.format(n,fact))           
# 5. Program End