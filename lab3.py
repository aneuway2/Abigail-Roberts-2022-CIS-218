"""
Abby does strings
"""

my_string = ( input ("Please type in string"))

vowel = 0
for c in my_string:
    if c in "AEIOUaeiou":
        print (c, "is a vowel")
        vowel += 1

lowercase = 0
for c in my_string:
    if "a" <= c <= "z":
        print (c, "is lowercase")
    else:
        print (c)
        lowercase += 1
               
    #print (c)

    uppercase = 0
    if "A" <= c <= "Z":
        print (c, "is uppercase")
        uppercase += 1

print ("There were ", vowel, " vowels ")

print ("There were ", lowercase, " lowercases ")

print ("There were ", uppercase, " uppercases ")

