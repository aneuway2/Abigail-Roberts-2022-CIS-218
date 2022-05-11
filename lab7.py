"""
Abigail Roberts
"""
height = float(input('enter height in inches: '))
weight = float(input('enter weight in lbs: '))

def body_mass_index(height, weight):
    bmi = weight/(height**2) * 703
    if bmi < 18.5:
        return 'Underweight', bmi

    elif bmi >= 18.5 and bmi < 25:
        return 'Normal'

    elif bmi >= 25 and bmi < 30:
        return 'Overweight', bmi

    elif bmi >= 30:
        return 'Obese', bmi

def test_category():
    assert body_mass_index(78, 280)=='Obese'
    
def test_bmi():
    assert body_mass_index(82, 160)==16.7

def main():
    test_check()
    print ("all ok")

if __name__=="__main__":
    main()

quote, bmi = body_mass_index(height, weight)
print ('your bmi is: {} and you are: {}' .format(bmi, quote))

