from katas.csv_minimalist import csv_str_to_table

CSV_STRING = """Name;Street;City;Age
Peter Pan;Am Hang 5;12345 Einsam;42
Maria Schmitz;Kölner Straße 45;50123 Köln;43
Paul Meier;Münchener Weg 1;87654 München;65"""

SOLUTION = """Name         |Street          |City         |Age|
-------------+----------------+-------------+---+
Peter Pan    |Am Hang 5       |12345 Einsam |42 |
Maria Schmitz|Kölner Straße 45|50123 Köln   |43 |
Paul Meier   |Münchener Weg 1 |87654 München|65 |"""


def test_csv():
    result = csv_str_to_table(CSV_STRING)
    print(result)
    assert result == SOLUTION
