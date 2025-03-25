s='good'
print(s*5)
print(s[0]*5,'\n')

x='India'
print(x=='India')
print(x=='india','\n')

print('apple'>'one') # o comes after a, hence considered bigger and not the other way round so o > a so this one is false 
print('four'<'ten','\n') #f comes before t so f < t so true

print('ab' < 'az')  #b comes before z so b<z so true
print('abcdef' < 'abcde','\n') # all letters same, f extra, f cannot come before nothing so this is false

p='python'
print(p[-1])
print(p[-2])
print(p[-3])
print(p[-4])
print(p[-5])
print(p[-6],'\n')

s='abcdefghijklmnopqrstuvwxyz'
print(len(s))