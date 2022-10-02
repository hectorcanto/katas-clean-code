from tabulate import tabulate

csv_string = """Name;Street;City;Age
Peter Pan;Am Hang 5;12345 Einsam;42
Maria Schmitz;Kölner Straße 45;50123 Köln;43
Paul Meier;Münchener Weg 1;87654 München;65"""


def csv_str_to_table(csv_str: str, field_break=";", row_break="\n"):
    new_table = [row.split(field_break) for row in csv_str.split(row_break)]
    return tabulate(new_table, headers="firstrow", tablefmt="orgtbl", numalign="left")
