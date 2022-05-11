"""
CIS-218 Final Exam
Abigail Roberts
"""

class Power (object):
    def __init__(self, name=0, megawatts=0, age=0, lifespan=60):
        """variables"""
        self.__name = name
        self.__megawatts = megawatts
        self.__age = age
        self.__lifespan = lifespan

    def set_name(self, name):
        self.__name = name

    def get_name(self, name):
        return self.__name

    def set_megawatts(self, megawatts):
        self.__megawatts = megawatts

    def get_megawatts(self, megawatts):
        return self.__megawatts

    def set_age(self, age):
        self.__age = age

    def get_age(self, age):
        return self.__age

    def set_lifespan(self, lifespan):
        self.__lifespan = lifespan

    def get_lifespan(self, lifespan):
        return self.__lifespan

    def capacity(self):
        #calculates capacity
        return self.__megawatts - (self.__megawatts / self.__lifespan * self.__age)
        print(round(self.__capacity))

    def available(self):
        if self.__capacity >= 0:
            return True
        else:
            return False

    def __str__(self):
        """
        Returns a human readable string
        """
        return "(" + str(self.__name) + "," + str(self.__capacity) + ")"

    def __repr__(self):
        """
        Return a complete representation of the object
        It is used for debugging and not designed for printing
        """
        return "Power(" + str(self.__name) + "," + str(self.__megawatts) + "," + str(self.__age) + "," + str(self.__lifespan) + ")"


class Wind(Power):
    """Wind is a subclass of Power"""
    def __init__(self, name=0, megawatts=0, age=0, lifespan=25):
        self.set_name(name)
        self.megawatts=megawatts
        self.age=age
        self._lifespan = lifespan

    def __str__(self):
        return "(" + str(self.__name) + "," + str(self.__capacity) + ")"


class Nuclear(Power):
    """Nuclear is a subclass of Power"""
    def __init__(self, name=0, megawatts=0, age=0, lifespan=60, coolingtowers=0):
        self.set_name(name)
        self.megawatts=megawatts
        self.age=age
        self._lifespan = lifespan
        self._coolingtowers = coolingtowers #This is a private variable

    def available(self):
        if capacity >= coolingtowers * 100:
            return True
        else:
            return False

def testcapacity_Wind(Power):
    W1 = Power()
    assert W1.get_megawatts() == 100
    assert W1.get_age() == 10
    assert W1.get_capacity() == 60

def testavailability_Wind(Power):
    W2 = Power()
    assert W2.get_megawatts() == 100
    assert W2.get_age() == 10

def testcapacity_Nuclear(Power):
    N1 = Power()
    assert N1.get_megawatts() == 600
    assert N1.get_age() == 10
    assert N1.get_coolingtowers() == 10
    assert N1.get_capacity() == 500

def testavailability_Nuclear(Power):
    N2 = Power()
    assert N2.get_megawatts() == 600
    assert N2.get_age() == 10
    assert N2.get_coolingtowers() == 10

def test__str__(Power):
    P1 = Power()
    assert P1.get_name() == TestWindPlant
    assert P1.get_age() == 0

def test__repr__(Power):
    P2 = Power()
    assert P2.get_name() == TestNuclearPlant
    assert P2.get_age() == 0

if __name__ == "__main__":
    power_plants = [
        Wind(name="Alta Wind Energy", megawatts=1320, age=12),
        Wind(name="Roscoe Wind Farm", megawatts=781, age=10),
        Wind(name="Shepherds Flat Wind Farm", megawatts=845, age=13),
        Nuclear(name="Palo Verde", megawatts=3942, age=36, coolingtowers=3),
        Nuclear(name="Browns Ferry", megawatts=3300, age=48, coolingtowers=6),
        Nuclear(name="South Texas", megawatts=2560, age=34, coolingtowers=0),
    ]
    available = [_ for _ in power_plants if _.available()]
    order = sorted(available, reverse=True, key=lambda plant: capacity())
    named_list = [str(_) for _ in order]
    print(named_list)

    
    
