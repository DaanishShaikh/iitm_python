# # xyz123@iitm.in

email = input()
for c in email:
    if (c == '@'):
        break
    print(c, end = '')



# xyz123@iitm.in

email = input()
for c in email:
    if (c == '@'):
        print('')
        continue
    print(c, end = '')



for x in range(11):
    if (x % 3 == 0):
        print(x)
    else:
        pass        #the pass command will not ignore the keyword like it ignores comments it will execute the keyword but will do nothing

