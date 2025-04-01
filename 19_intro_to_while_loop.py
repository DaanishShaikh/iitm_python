print("When did India get its independence (year)?")
year = int(input())

if (year == 1947):
    print("Hip Hip Hurray. You got that right!")
else:
    print("Comeon dont you know even this?")
    print("Thats ok, I will let you attempt this once more")
    print("When did India get its independence?")
    year = int(input())
    if (year == 1947):
        print("You got it!")
    else:
        print("Failed in your second attempt too? grrrr...")

print("When did India get its independence (year)?")
year = int(input())

while(year != 1947):
    print("You got this wrong. Enter once again.")
    year = int(input())

print("Wowwwww... you got it right! 1947")

# while works like this:
# while <condition>
#     write whatever you want here
#     write whatever you want here
#     write whatever you want here
