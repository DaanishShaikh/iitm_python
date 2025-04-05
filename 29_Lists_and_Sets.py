# sets have only unique elements and the elements are arranged in ascending order 
# sets take longer time time to form than lists
# for example lets say that we form a list l=list(range(1000000000)) meaning the list will have that many members or space then the 
# computer makes the list and as the no. of elements is so high it takes anywhere from 5 to 10 seconds which is not normal as normally 
# the computer does stuff within a second
# now but when you do the same thing with a set that is you make a set with that many elements lets say s=set(range(1000000000)) it aint 
# even gonna take a few seconds, it will literally take more than a whole minute to form.

# but the interesting thing is that when in the same list l, you try to do this command -1 in l, it will take almost a minute to give the 
# output as it will look into each of the millions of elements that it has
# but if you try to look for a -1 in set lets say then it will give out the output in less than a second, this is because in a set every 
# thing is arranged in an ascending order and this helps it to use various fast techniques like binary search etc which reduces the time
# required to scan through the entire set

# in interactinve python shells lets say if z is a set then z.add? will give the explaination of what the method add does to a set

# a set is not subscriptable which means that unlike in list when you type l[0] you will get the element as the output but a set is not 
# subscriptable which means that when you type s[0] then it will give an error

# hence set is good for situations in which you need to store data where you dont wanna retrieve it but just wanna check if its there or
# not 
# for example
# lets say you are making a list of countries that you have visited, you dont really care which sequence you have visited the countries in
# all you care is that you get to know if a country is visited or not, for example you will put the names of the countries in a set like 
# this s={india, america, japan, china , north korea} now you just wanna know if you have visited china, so you just type 'china' in s 
# and it will give true, if you type 'mongolia' in s then it will give false and this is all you need, it will give answet very very fast
# when compared to list this is why you use set for this purpose

#s.add(mongolia) will add 'mongolia' to your set