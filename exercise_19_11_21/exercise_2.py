import math  # til brug af gcd metode 

class Rational:
    """
    A class representing a rational number (fraction)

    fields:
        + numerator: int
        + denominator: int
    methods:
        + add(Rational): Rational
        + sub(Rational): Rational
        + mul(Rational): Rational
        + div(Rational): Rational
        + invert(Rational): Rational
        + negate(): Rational
        + reduce(): Rational
        + cmp(Rational): int
        + numeric(): float
    dunder methods:
        + __gt__(Rational): bool
        + __lt__(Rational): bool
        + __eq__(Rational): bool
        + __str__(): str
        + __repr__(): str
    """

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def add(self, other):
        # Fx: 1/4 + 3/8 => 1*8/4*8 + 3*4/8*4 => 8/32 + 12/32 => 20/32 - Herefter brug af .reduce metoden
        new_numerator = self.numerator * other.denominator + \
            other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator).reduce() 

    def sub(self, other):
        # Fx: 1/4 - 3/8 => 1*8/4*8 - 3*4/8*4 => 8/32 - 12/32 => -4/32 - Herefter brug af .reduce metoden
        new_numerator = self.numerator * other.denominator - \
            other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator).reduce() 

    def mul(self, other):
        # Fx: 1/4 * 3/8 => (1*3)/(4*8) => 3/32 - Herefter brug af .reduce metoden
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator).reduce() 

    def div(self, other):
        # Fx: 1/4 / 3/8 => (1*8)/(4*3) => 8/12 - Herefter brug af .reduce metoden
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Rational(new_numerator, new_denominator).reduce() 

    def invert(self):
        # Fx: 1/4 => 4/1
        return Rational(self.denominator, self.numerator) # bør ikke automatisk reduceres efter min mening
    def negate(self):
        # Fx: 1/4 => -1/4
        return Rational(-self.numerator, self.denominator) # bør ikke automatisk reduceres efter min mening

    def reduce(self):
        # Fx: 4/8 => 1/2
        gcd = math.gcd(self.numerator, self.denominator)  # finder gcd => største fælles nævner
        # dividerer både tæller og nævner med gcd
        return Rational(self.numerator // gcd, self.denominator // gcd)

    def cmp(self, other):
        # Fx: 1/4 cmp 3/8 => 1*8 cmp 3*4 => 8 cmp 12 => -1
        # Fx: 1/4 cmp 1/4 => 1*4 cmp 1*4 => 4 cmp 4 => 0
        # Fx: 3/8 cmp 1/4 => 3*4 cmp 1*8 => 12 cmp 8 => 1
        if self.numeric() < other.numeric():
            return -1
        elif self.numeric() == other.numeric():
            return 0
        else:
            return 1

    def numeric(self):
        return self.numerator / self.denominator
    # Bare for sjov tilføjede jeg dunder-metoderne, så det faktisk er muligt at bruge >, <, == på objekterne :-)
    def __gt__(self, other):
        return self.cmp(other) == 1

    def __lt__(self, other):
        return self.cmp(other) == -1

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Rational({self.numerator}, {self.denominator})"
