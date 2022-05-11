"""
Tests the expected functionality of the Final Exam
"""

from power import Power, Wind, Nuclear


def str_equal(expected: str, actual: str) -> str:
    """
    Helper method that compares two strings and removes non functional
    comparisons like text case and spaces
    """

    def stripped(string: str) -> str:
        return str(string).lower().replace(" ", "")

    print(f'\tTEST: "{expected}" == "{actual}"')
    if isinstance(expected, str) and isinstance(actual, str):
        expected = stripped(expected)
        actual = stripped(actual)
    return expected == actual


DEFAULT_ATTRS = {"name": "Test", "megawatts": 0, "age": 0}


def test_expected_power_class():
    """
    Create a class called Power. This class should set variables for
    name, megawatts, age, and lifespan when initialized using parameters
    of the same name. The lifespan parameter should be set to 60 years
    by default.
    """
    expected = DEFAULT_ATTRS
    plant = Power(**expected)
    for attr in expected:
        assert hasattr(plant, attr)
        assert getattr(plant, attr) is not None
    assert plant.lifespan == 60


def test_expected_wind_capacity():
    """
    Test for Wind Power Plant capacity

    Create a method within Power called capacity, which calculates the
    actual amount of electricity the power plant can produce based on age.
    The electric company has defined this calculation as
    megawatts – (megawatts / lifespan * age) and should be rounded to the
    nearest whole number and a non-negative number.
    """
    capacity = Wind("Test", 100, 10).capacity()
    assert capacity == 60


def test_expected_wind_availability():
    """
    Test for Wind Power Plant availability

    Create another method within Power called available, which returns True
    if the capacity is greater than 0 or False if otherwise.
    """
    plant_available = Wind("Test", 100, 10).available()
    assert plant_available

    plant_unavailable = Wind("Test", -1, 1).available()
    assert not plant_unavailable


def test_expected_str():
    """
    Test Wind Power Plant's str()

    You should also add a __str__ method that returns the name of the power
    plant and its capacity.
    """
    wind_plant = str(Wind(name="Test Wind Plant", megawatts=100, age=0))
    assert str_equal(wind_plant, "Test Wind Plant (100 MW)")


def test_expected_repr():
    """
    Test Nuclear Power Plant's repr()

    Also include a __repr__ method that displays the representation of the
    Power class.
    """
    expected = {
        "name": "Test Nuclear Plant",
        "megawatts": 100,
        "age": 0,
    }
    nuclear_plant = repr(Nuclear(**expected, cooling_towers=0))

    for key, value in expected.items():
        assert key in nuclear_plant
        assert str(value) in nuclear_plant


def test_expected_wind_class():
    """
    Create a subclass of Power called Wind. The Wind class inherits all the
    methods from the Power class; however, its lifespan parameter
    should be 25 when initialized.
    """
    expected = DEFAULT_ATTRS
    plant = Wind(**expected)
    for attr in expected:
        assert hasattr(plant, attr)
        assert getattr(plant, attr) is not None
    assert plant.lifespan == 25


def test_expected_nuclear_class():
    """
    Create a subclass of Power called Nuclear. The Nuclear class inherits
    from the Power class and should also allow an additional parameter
    called cooling_towers to be set when initialized which stores
    its value as a private variable.
    """
    expected = {**DEFAULT_ATTRS, "cooling_towers": 0}
    plant = Nuclear(**expected)
    for attr in expected:
        if attr == "cooling_towers":
            # https://docs.python.org/3/reference/expressions.html#private-name-mangling
            attr = "_Nuclear__cooling_towers"
        assert hasattr(plant, attr)
        assert getattr(plant, attr) is not None


def test_expected_nuclear_capacity():
    """
    Test for Nuclear Power Plant capacity

    To prevent meltdowns, the local power company has also defined that the
    available methods’ calculation should be True if
    capacity >= cooling_towers * 100 and should be rounded to the nearest
    whole number and a non-negative number.
    """
    capacity = Nuclear("Test", 600, 10, 10).capacity()
    assert capacity == 500


def test_expected_nuclear_availability():
    """Test for Nuclear Power Plant availability"""
    plant_available = Nuclear("Test", 600, 10, 10).available()
    assert not plant_available


def test_expected_functional():
    """A functional test of the system"""
    test_power_plants = [
        Wind(name="Alta Wind Energy", megawatts=1320, age=12),
        Wind(name="Roscoe Wind Farm", megawatts=781, age=10),
        Wind(name="Shepherds Flat Wind Farm", megawatts=845, age=13),
        Nuclear(name="Palo Verde", megawatts=3942, age=36, cooling_towers=3),
        Nuclear(name="Browns Ferry", megawatts=3300, age=48, cooling_towers=6),
        Nuclear(name="South Texas", megawatts=2560, age=34, cooling_towers=0),
    ]
    test_available = [_ for _ in test_power_plants if _.available()]
    test_order = sorted(
        test_available, reverse=True, key=lambda plant: plant.capacity()
    )
    test_named_list = [str(_) for _ in test_order]
    expected = [
        "Palo Verde (1577 MW)",
        "South Texas (1109 MW)",
        "Alta Wind Energy (686 MW)",
        "Browns Ferry (660 MW)",
        "Roscoe Wind Farm (469 MW)",
        "Shepherds Flat Wind Farm (406 MW)",
    ]
    for index, _ in enumerate(test_named_list):
        assert str_equal(expected[index], test_named_list[index])
