a='onomotopia'
b='mitochondria'
print('1 ',a+b) #concatenates the two strings output=onomotopiamitochondria
print('2 ',a[1])
print('3 ',b[0])
print('4 ',a[1:5])#this will print the letters from s[1] to s[5-1]==s[4], point to be noted here is that it goes till n-1 and not n
#output=nomo

s='0123456789'
x=s[7]
y=s[8]
print('5 ',x+y) #will concatenate the two characters and wont sum them output=78
c=int(s[7]) #so in python we can easily change a numeric string into an integer data type
d=int(s[8])
print('6 ',c+d) #this time they arent characters anymore, they are integers so normal arithmatic operation will work output=15

print('7 ',s*5) #this concatenates the string with itself, 5 times
print('8 ',s[6]*5) #this will concatenate the chosen character with itself, 5 times

i='India' #in python we can use '' for strings as well
print('9 ',i=='India') #how string comparison works in python
print('10 ',i=='india')

print('11 ','apple'>'one') #this is done as the compiler compares the first letters that is a and o, and as o comes after a, o>a/a<0
print('12 ', 'four'<'ten') #again first letters ie f and t are compared, t comes after f so t>f, so f<t
print('13 ', 'ab'<'az') #as first letters are same, second letters i.e. b and z are compared, and hence z>a or a<z
print('14 ', 'abcdef'<'abcde') #here the first 5 letters are same so the 6 letter are compared
#as 6th letter of first string is there, and it is not there in second string, f cant be smaller than nothing, so f>nothing

print(s[-1]) #this is reverse indexing and -1 points to the last character of the string
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
print(s[-6])
print(s[-7])
print(s[-8])
print(s[-9])
print(s[0])

print(len(s)) #the len functions tells us the size of a string
print(s[len(s)-1]) #this way we can easily print the last letter of a string, or simply trype s[-1] yaar