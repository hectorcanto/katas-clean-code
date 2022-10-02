"""Solution of Decimal to Roman Kata in python

Discussion:
ROMAN_LITERALS could be a tuple of tuples or a dict
order is not ideal, maybe encapsulate in a Class or break into modules
launcher is not the best name, but is a convention

"""
import pytest
import argparse


ERROR_MSG = "Invalid decimal number"
# fmt: off
ROMAN_LITERALS = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
    (1, "I"),
]
# fmt: on


def transform_decimal_to_roman(number: int) -> str:
    roman_cipher_list = []
    remaining = number  # NOTE remaining is the right name for the loop
    for decimal, literal in ROMAN_LITERALS:
        while remaining >= decimal:
            remaining -= decimal
            roman_cipher_list.append(literal)
    return "".join(roman_cipher_list)


def present_result(decimal, roman):
    print(f"{decimal}  => {roman}")


def check_valid_decimal(decimal):
    if not isinstance(decimal, int):
        raise ValueError(f"{ERROR_MSG}: {decimal}")
    if decimal > 3000 or decimal < 1:
        raise ValueError(f"{ERROR_MSG}: {decimal}")


def launcher(decimal: int):
    """Convert an integer into a Roman numeral

    Args: A integer between
    Raises: ValueError if decimal is not int or is out of [1,3000]

    Run: python3 -m kata_roman.launcher
    """
    # TODO get input through arguments with __main__
    check_valid_decimal(decimal)
    partial_result = transform_decimal_to_roman(decimal)
    present_result(decimal, partial_result)
    return partial_result
