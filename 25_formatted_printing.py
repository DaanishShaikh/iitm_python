for x in range(10):
    print(x , end = ' ' )   #this is how you print on the same line
print('\n')

d = 10
m = 5
y = 2021
print("Today's date is", end = ' ') #if you write print("Today's date is", d, m, y, sep = '/') then output Today's date is/10/5/2021
print(d, m, y, sep = '/')

print('\n')

print("Enter the number you want multiples of:- ",end=' ')
num = int(input())
for i in range(1, 11):
    #print(num, 'X', i, '=', num * i)          #different ways of writing same line
    #print(f'{num} X {i} = {num * i}')
    #print('{0} X {1} = {2}'.format(num, i, num * i))
    print('%d X %d = %d' % (num, i, num * i))

print('\n')

pi = 22 / 7

print(f'Value of PI = {pi}')
print('Value of PI = {0}'.format(pi))
print('Value of PI = %f' % (pi))

print('\n')

pi = 22 / 7

print(f'Value of PI = {pi:.2f}') # f denotes float that is the datatype and the number before f denotes no. of decimal spaces you wanna display
print('Value of PI = {0:.3f}'.format(pi))
print('Value of PI = %.4f' % (pi))

print('\n')

print('{0:5d}'.format(1)) #d denotes integer i.e. datatype and the no. before d denotes no of characters you need to have in a line
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(11111))

