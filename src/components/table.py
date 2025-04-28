import csv
import re
import textwrap

from tabulate import tabulate

import constants


def get_row_val(row, headers, header):
    return row[headers.index(header)]


def set_row_val(row, headers, header, val):
    row[headers.index(header)] = val


def filter(table, all_headers, selected_headers):
    return [
        [get_row_val(row, all_headers, header) for header in selected_headers]
        for row in table
    ]


def create():
    # Read CSV
    with open(constants.PROJECTS_CSV, encoding="utf-8") as csvfile:
        csvlist = list(csv.reader(csvfile, delimiter=",", quotechar='"'))
        headers, projects = csvlist[0], csvlist[1:]

    # Create formatted table
    selected_headers = ["Title", "Description"]
    filtered = filter(projects, headers, selected_headers)

    for row in filtered:
        title_old = get_row_val(row, selected_headers, "Title")
        descr_old = get_row_val(row, selected_headers, "Description")

        title_new = f"~{title_old}~"
        descr_new = textwrap.fill(descr_old, width=constants.DESCR_WIDTH)

        set_row_val(row, selected_headers, "Title", title_new)
        set_row_val(row, selected_headers, "Description", descr_new)

    table_str = tabulate(
        filtered,
        headers=["Title", "Description"],
        tablefmt=constants.TABLE_STYLE,
        showindex=False,
    )

    # Replace 'Title' with hyperlinked text
    for row in projects:
        repo = get_row_val(row, headers, "Repo")
        title = get_row_val(row, headers, "Title")
        regex = re.escape(f"~{title}~").replace(r"\ ", r"\s+")
        replacement = (
            f'<a href="https://github.com/mbeardwell/{repo}">{title}</a>' + " " * 2
        )
        table_str = re.sub(regex, replacement, table_str, flags=re.DOTALL)

    with open(constants.TABLE_MD, "w", encoding="utf-8") as mdfile:
        mdfile.write(table_str + "\n")
