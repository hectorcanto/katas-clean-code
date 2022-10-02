FIELD_BREAK = ";"
ROW_BREAK = "\n"
SPACE = " "
BAR = "|"
DASH = "-"
PLUS = "+"


def extract_info_from_csv(raw_csv: str):

    header, all_rows = raw_csv.split(ROW_BREAK, 1)
    row_list = all_rows.split(ROW_BREAK)
    field_names = header.split(FIELD_BREAK)

    nice_rows = list()
    for raw_row in row_list:
        value_list = raw_row.split(FIELD_BREAK)
        row_mapping = {field: value for field, value in zip(field_names, value_list)}
        nice_rows.append(row_mapping)
        # Mapping could be a list, as order is not modified

    return field_names, nice_rows


def format_line(fields: list, width_per_column: list, filler=SPACE, column_break=BAR):
    modified_fields = [field.ljust(width, filler) for field, width in zip(fields, width_per_column)]
    return column_break.join(modified_fields) + column_break


def format_header(header_fields, column_width):
    header = format_line(header_fields, column_width)
    separator = format_line(["-"] * len(header_fields), column_width, DASH, PLUS)
    return "\n".join([header, separator])


def format_body(row_mappings, column_width):
    formatted_lines = [format_line(one_line.values(), column_width) for one_line in row_mappings]
    return "\n".join(formatted_lines)


def compute_width(headers, row_mapping):
    row_values = [[value for value in row.values()] for row in row_mapping]
    all_row_values = [headers] + row_values

    width_per_column = []
    for index, _ in enumerate(headers):
        all_column_width = [len(row[index]) for row in all_row_values]
        width_per_column.append(max(all_column_width))
    return width_per_column


def format_table(header_fields: list, rows: list):
    width_per_column = compute_width(header_fields, rows)
    nice_header = format_header(header_fields, width_per_column)
    nice_body = format_body(rows, width_per_column, column_order=header_fields)
    return nice_header + "\n" + nice_body


def main(raw_csv):
    headers, rows = extract_info_from_csv(raw_csv)
    result = format_table(headers, rows)
    print(result)
    return result
