"""
Abigail Roberts
"""
height = float(input('enter height in inches: '))
weight = float(input('enter weight in lbs: '))

def BMI(height, weight):
    bmi = weight/(height**2) * 703
    if (bmi < 18.5):
        return 'Underweight', bmi

    elif (bmi >= 18.5 and bmi < 25):
        return 'Normal'

    elif (bmi >= 25 and bmi < 30):
        return 'Overweight', bmi

    elif (bmi >= 30):
        return 'Obese', bmi

def check():
    def test_check():
        assert check.check (82, 160)==16.7
        assert check.check (78, 280)==Obese

def main():
    test_check()
    print ("all ok")

if __name__=="--main--":
    main()

quote, bmi = BMI(height, weight)
print ('your bmi is: {} and you are: {}' .format(bmi, quote))

