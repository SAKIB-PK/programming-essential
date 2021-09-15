# 1. Program start 
# 2. Take variable n value
n = int(input())
# 3. initial sum variable to store sum n series
sum = 0
# 4. for loop 1 to n times
# N.B check n value
if n<=0:
    print('Please give me a positive integer value.')
else : 
    for i in range(1,n+1):
        # 5. sum all the value 1 to n 
        sum +=i 
    # Then print sum value 
    print('The ans is = {}'.format(sum))
         
