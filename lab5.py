"""
Sample Functions
"""

my_dict = {
    212: "boiling point",
    32: "freezing point",
}

user_input = 32
user_input = 212

if my_dict.get(user_input):
    print(my_dict.get(user_input))


def celsius_to_fahr(celsius=0):
    """
    Apx. fahr = (celsius * 9/5) + (32))
    """
    fahr = celsius * 9 / 5 + 32
    print(f" {fahr} degrees Fahrenheit is returned from the celsius_to_fahr function")
    return fahr


def test_celsius_to_fahr():
    """
    Tests the celsius_to_fahr function
    """
    assert celsius_to_fahr() == 32.0
    assert celsius_to_fahr(10) == 50.0
    assert celsius_to_fahr(24) == 75.2
