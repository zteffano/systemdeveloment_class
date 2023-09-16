from exercise_2 import Rational

"""
Simpel Test cases for en Rational class ved brug af AAA (Arrange, Act, Assert) pattern
"""


def test_constructor():
    # ARRANGE
    frac = Rational(1, 2)

    # ACT

    # ASSERT
    assert frac.numerator == 1
    assert frac.denominator == 2


def test_add():
    # ARRANGE
    frac1 = Rational(1, 2)
    frac2 = Rational(1, 2)
    frac3 = Rational(1, 4)
    frac4 = Rational(1, 4)

    # ACT
    result1 = frac1.add(frac2)
    result2 = frac3.add(frac4)

    # ASSERT
    assert result1.numerator == 1
    assert result1.denominator == 1
    assert result2.numerator == 1
    assert result2.denominator == 2


def test_sub():
    # ARRANGE
    frac1 = Rational(3, 4)
    frac2 = Rational(2, 8)

    # ACT
    result = frac1.sub(frac2)  # 3/4 - 2/8 = 6/8 - 2/8 = 4/8 = 1/2

    # ASSERT
    assert result.numerator == 1
    assert result.denominator == 2


def test_mul():
    # ARRANGE
    frac1 = Rational(1, 2)
    frac2 = Rational(1, 2)

    # ACT
    result = frac1.mul(frac2)

    # ASSERT
    assert result.numerator == 1
    assert result.denominator == 4


def test_div():
    # ARRANGE
    frac1 = Rational(1, 2)
    frac2 = Rational(1, 2)

    # ACT
    result = frac1.div(frac2)

    # ASSERT
    assert result.numerator == 1
    assert result.denominator == 1


def test_invert():
    # ARRANGE
    frac1 = Rational(1, 2)
    frac2 = Rational(2, 1)

    # ACT
    result1 = frac1.invert()
    result2 = frac2.invert()

    # ASSERT
    assert result1.numerator == 2
    assert result1.denominator == 1
    assert result2.numerator == 1
    assert result2.denominator == 2


def test_negate():
    # ARRANGE
    frac1 = Rational(1, 2)
    frac2 = Rational(-1, 2)

    # ACT
    result1 = frac1.negate()
    result2 = frac2.negate()

    # ASSERT
    assert result1.numerator == -1
    assert result1.denominator == 2
    assert result2.numerator == 1
    assert result2.denominator == 2


def test_reduce():
    # ARRANGE
    frac1 = Rational(2, 4)
    frac2 = Rational(1, 2)
    frac3 = Rational(10, 25)

    # ACT
    result1 = frac1.reduce()
    result2 = frac2.reduce()
    result3 = frac3.reduce()

    # ASSERT
    assert result1.numerator == 1
    assert result1.denominator == 2
    assert result2.numerator == 1
    assert result2.denominator == 2
    assert result3.numerator == 2
    assert result3.denominator == 5


def test_cmp():
    # ARRANGE
    frac1 = Rational(1, 2)
    frac2 = Rational(1, 2)
    frac3 = Rational(1, 4)

    # ACT
    result1 = frac1.cmp(frac2)
    result2 = frac1.cmp(frac3)
    result3 = frac3.cmp(frac1)

    # ASSERT
    assert result1 == 0
    assert result2 == 1
    assert result3 == -1
