a1=5
a1_=5
# no error as all this will work
# uppercase and lower case matters as well

# multiple assignment
x , y = 1 , 2
print(x,y)
x , y = y , x
print(x,y,'\n')   # swapping variables

# deleting variables
x=10
print(x,'\n')
del x
# print(x)

# searching a word in a searching
print('alpha' in 'A variable name can only contain alpha-numeric characters and underscores') 
print('alpha' in 'A variable name must start with a letter or the underscore character','\n')

# multiple operators
x = 5
print(1 < x < 10)
print(10 < x < 20)
print(x < 10 < x * 10 < 100)
print(10 > x <= 9)
print(5 == x > 4)
