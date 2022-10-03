from katas.csv import compute_width, extract_info_from_csv, main, format_header
from .test_csv_minimal import CSV_STRING, SOLUTION


def tests_width():
    header, rows = extract_info_from_csv(CSV_STRING)
    width_per_column = compute_width(header, rows)
    expected = [13, 16, 13, 3]
    assert width_per_column == expected


def test_format_header():
    header = ["a", "b", "c"]
    width = [2, 2, 2]
    result = format_header(header, width)
    assert result == "a |b |c |\n--+--+--+"


def test_e2e():
    result = main(CSV_STRING)
    assert result == SOLUTION
