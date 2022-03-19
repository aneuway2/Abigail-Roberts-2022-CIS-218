def check (num1, num2=0, tol=.1):
    """
    Compares num1 and num2 and returns true if the absolute difference
    id less than or equal to tol.
    num2 defaults to 0
    tol defaults to .1

    """
    if abs(num1 - num2) <= tol:
        return True
    return False


def test_check():
    assert check(.1)
    assert check(.1001)==False
    assert check(.5, .5999)
    assert check(.5999, .5)
    assert check(-.5, -.5999)
    assert check(-.5, .5)==False
    assert check(.5, tol=.5001)
    assert check(.02, tol=.001)==False

def main():
    test_check()
    print ("OK, you did it!")

if __name__ == "__main__":
    main()



