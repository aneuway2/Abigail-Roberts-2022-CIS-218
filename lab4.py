"""
Abigail Roberts
"""

my_dict = {
    "mother": "A woman in relation to her child",
    "zebra": "An African wild horse",
    "penny": "One cent is one hundredth of a dollar",
}

while True:

    user_input = ( input ("Please type in a word"))

    #This line is a comment

    if my_dict.get(user_input):
        print (my_dict.get(user_input))
    else:
        new_input = ( input ("Would you like to add?"))
        if new_input == "yes":
            new_input = "flower"
        my_dict.update({"mother":
"flower"})
        print ("Updated")
