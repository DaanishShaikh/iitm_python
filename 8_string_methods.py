x='pYtHon sTriNg MetHoDS'
print(x.lower())                #lower
print(x.upper())                #upper
print(x.capitalize())           #capitalize
print(x.title())                
print('swapcase',x.swapcase())
a='python'
print('islower',a.islower())
b='Python'
print(b.islower())
a='PYTHON'
print(a.isupper())
b='PYTHoN'
print(b.isupper())
a='Python String Methods'
print(a.istitle())
a='12345'
print(a.isdigit())
a='1234ghjk'
print(a.isdigit())
a='1234ghjk'
print(a.isalpha())
a='ghjk'
print(a.isalpha())
a='1234ghjk'
print(a.isalnum())   #alnum = alpha numeric
a='1234ghjk%^%^'
print(a.isalnum())
a='----Python----'
print(a.strip('-'))
print(a.lstrip('-'))
print(a.rstrip('-'))
a='python'
print(a.startswith('p'))
print(a.startswith('P'))
print(a.endswith('n'))
print(a.endswith('N'))
x='Python String Methods'
print(x.count('t'))
print(x.index('t'))
print(x.replace('P','D'))
