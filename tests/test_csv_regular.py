from katas.csv import compute_width, extract_info_from_csv, main


def tests_width():
    header, rows = extract_info_from_csv(csv_string)
    width_per_column = compute_width(header, rows)
    expected = [13, 16, 13, 3]
    assert width_per_column == expected


def test_format_header():
    header = ["a", "b", "c"]
    width = [2, 2, 2]
    result = format_header(header, width)
    assert result == "a |b |c |\n--+--+--+"


# TODO solution is used in another test, move to common
SOLUTION = """Name         |Street          |City         |Age|
-------------+----------------+-------------+---+
Peter Pan    |Am Hang 5       |12345 Einsam |42 |
Maria Schmitz|Kölner Straße 45|50123 Köln   |43 |
Paul Meier   |Münchener Weg 1 |87654 München|65 |"""


def test_e2e():
    result = main(csv_string)
    assert result == SOLUTION
