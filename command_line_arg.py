import sys
print("Command Length : ",len(sys.argv))
print('Command List is : ', str(sys.argv))
x = sys.argv[1]
y = sys.argv[2]
print('The file name is : ', sys.argv[0])
z=int(x) + int(y)
print('x: {} y: {} \n sum of x and y: {} '.format(x,y,z))

