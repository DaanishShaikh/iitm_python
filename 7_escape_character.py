#print('it's a good day')       #this line will give an error, as the ' sign in the string will 
                                #make it think that this is the single qoute for the strings
print('it\'s a good day')       #here the single quotation doesnt through an error

#print("i love "iit" madras")   #this wont work, it will give error
print("i love \"iit\" madras")  #this will work

print("my name is daanish. i am from mumbai")
print("my name is daanish.\ti am from mumbai") #the \t in the code will leave a tab worth of space so it will leave 8 spaces
print("my name is daanish.\ni am from mumbai") #here the \n will leave a line

x='something1'
y='something2'
#now what if we need to store a variable in multiple line like this:
#z='first
#second
#third
#fourth'
#we do it with triple quotes(''') instead of single quote
z='''first
second
third
fourth'''
print(x)
print(y)
print(z)