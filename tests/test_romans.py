import pytest

from katas.roman_numbers import transform_decimal_to_roman, launcher


@pytest.mark.parametrize(
    "decimal, roman",
    (
        (1, "I"),
        (2, "II"),
        (4, "IV"),
        (5, "V"),
        (9, "IX"),
        (13, "XIII"),
        (42, "XLII"),
        (99, "XCIX"),
        (2512, "MMDXII"),
        (3000, "MMM"),
    ),
)
def test_kata_roman_good(decimal, roman):
    assert transform_decimal_to_roman(decimal) == roman


@pytest.mark.parametrize("bad", ((None, "aaa", 0, -1, 4000, 2.5)))
def test_kata_roman_fails(bad):
    with pytest.raises(ValueError):
        launcher(bad)
