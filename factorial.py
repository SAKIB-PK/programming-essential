# 1. Programme start 
# 2. input n value 
fact =1;
n = int(input())
# if n <0 then print 'Negative value are not allowed
if n<0:
    print('Negative numbers are not allowed. ')
# if n=0 or n=1 then fact value 1 
else: 
    if (n==1 or n==0): 
        print('Fact = {}'.format(fact))
    else:
        # 3. when n value are bigger then 1 then create a loop and excute fact = fact +1
        for i in range(2,n+1):
            fact *=i
    # then print value
    print(fact)           
    