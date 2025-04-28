import csv
import re
import textwrap
from typing import List

from tabulate import tabulate

import constants


def get_row_val(row: List[str], headers: List[str], header: str) -> str:
    return row[headers.index(header)]


def set_row_val(row: List[str], headers: List[str], header: str, val: str) -> None:
    row[headers.index(header)] = val


def filter_table(
    table: List[List[str]], all_headers: List[str], selected_headers: List[str]
) -> List[List[str]]:
    return [
        [get_row_val(row, all_headers, header) for header in selected_headers]
        for row in table
    ]


def create() -> None:
    # Read CSV
    with open(constants.PROJECTS_CSV, encoding="utf-8") as csvfile:
        csvlist: List[List[str]] = list(
            csv.reader(csvfile, delimiter=",", quotechar='"')
        )
        headers: List[str] = csvlist[0]
        projects: List[List[str]] = csvlist[1:]

    # Create formatted table
    selected_headers: List[str] = ["Title", "Description"]
    filtered: List[List[str]] = filter_table(projects, headers, selected_headers)

    for row in filtered:
        title_old: str = get_row_val(row, selected_headers, "Title")
        descr_old: str = get_row_val(row, selected_headers, "Description")

        title_new: str = f"~{title_old}~"
        descr_new: str = textwrap.fill(descr_old, width=constants.DESCR_WIDTH)

        set_row_val(row, selected_headers, "Title", title_new)
        set_row_val(row, selected_headers, "Description", descr_new)

    table_str: str = tabulate(
        filtered,
        headers=["Title", "Description"],
        tablefmt=constants.TABLE_STYLE,
        showindex=False,
    )

    # Replace 'Title' with hyperlinked text
    for row in projects:
        repo: str = get_row_val(row, headers, "Repo")
        title: str = get_row_val(row, headers, "Title")
        regex: str = re.escape(f"~{title}~").replace(r"\ ", r"\s+")
        replacement: str = (
            f'<a href="https://github.com/mbeardwell/{repo}">{title}</a>' + " " * 2
        )
        table_str = re.sub(regex, replacement, table_str, flags=re.DOTALL)

    with open(constants.TABLE_MD, "w", encoding="utf-8") as mdfile:
        mdfile.write(table_str + "\n")
